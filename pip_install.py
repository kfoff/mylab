#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

import json

with open('../mylab.json') as json_file:
    data = json.load(json_file)
    for p in data['pip']:
        print(p)  # noqa
        subprocess.call(['pip3', 'install', p])
