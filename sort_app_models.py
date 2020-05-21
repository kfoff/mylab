#!/usr/bin/env python3

from sort_app_inc import DependencyOrder
import re
from os.path import isfile
from os.path import join
from os import listdir
import sys


try:
    sys.argv[1]
except Exception:
    PATH = '/home/www/dpub'
else:
    PATH = sys.argv[1]

# we search for a model between to="model"
REGEX_MODEL_NAME = re.compile('(?<=to=")[^<:]+(?=")')


def read_the_xmls(xmls):
    """
    The following function takes all the xmls that are dump of the django
    database and places them in the special dictionary

    xmls - a list of paths to xmls
    """

    xmls.sort()

    model_with_depends = dict()

    for xml in xmls:

        file = open(PATH + '/' + xml, 'r')
        lines = file.readlines()

        # a list for collecting a list of dependencies
        dependencies = []

        for line in lines:

            # if we find one of dependencies
            if 'ManyToOneRel' in line \
                    or 'ManyToManyRel' in line \
                    or 'OneToOneRel' in line:
                matched_model = re.search(REGEX_MODEL_NAME, line).group()

                if matched_model != xml[:-4]\
                        and matched_model not in dependencies:
                    # in case it's not the same model
                    dependencies.append(matched_model)

            # if a model didn't contain anything
            if '</django-objects>' in line:
                model_with_depends[xml[:-4]] = dependencies
                break

    return model_with_depends


def sort_models(model_with_depends, dependency_order=None):
    """
    Sort the models according to their dependencies
    """

    if not dependency_order:
        dependency_order = DependencyOrder()

    for model, depends in model_with_depends.items():
        dependency_order.append(model, dependencies=depends)

    return dependency_order


def check_function(model_with_depends, dependency_order):
    """
    Check that the sort_models function sorted our models correctly
    """

    for model, depends in model_with_depends.items():
        for depend in depends:
            if dependency_order.index(model) < dependency_order.index(depend):
                return False

    return True


def deep_sort(model_with_depends):
    """
    Function that manages the check_function and sort_models
    """

    sorted_order = sort_models(model_with_depends)

    # max amount of tries
    count = 0

    while not check_function(model_with_depends, sorted_order) and count < 20:
        sorted_order = sort_models(model_with_depends, sorted_order)
        count += 1

    if count == 20:
        raise Exception("The xmls are impossible to sort")
    else:
        return sorted_order


if __name__ == "__main__":

    xmls = [f for f in listdir(PATH) if isfile(join(PATH, f))]

    # read the xmls
    model_with_dependencies = read_the_xmls(xmls)

    # order models
    proper_order = deep_sort(model_with_dependencies)

    # print the models
    print(*proper_order, sep=':', end='')
