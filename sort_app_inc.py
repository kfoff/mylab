"""
This module contains a class that helps keep the order of dependencies
(it's helpful when you need to install apps that have dependencies for
example)

>>> dependency_order = DependencyOrder()
>>> dependency_order.append('kitkat', dependencies=('snickers', 'nesquik'))
>>> dependency_order
['snickers', 'nesquik', 'kitkat']
>>> dependency_order.append('snickers', dependencies=('nesquik', 'milkyway'))
>>> dependency_order
['nesquik', 'milkyway', 'snickers', 'kitkat']
>>> dependency_order.append('mars')
>>> dependency_order
['mars', 'nesquik', 'milkyway', 'snickers', 'kitkat']
>>> dependency_order.append('coffee', dependencies=('sugar', 'nesquik'))
>>> dependency_order
['mars', 'nesquik', 'milkyway', 'snickers', 'kitkat', 'sugar', 'coffee']
"""


class DependencyOrder(list):
    """
    List that keeps the order of dependencies
    """

    def append(self, node, dependencies=tuple()) -> None:
        """Override the append method"""

        if node not in self:
            if not dependencies:
                # if there are no dependencies, we can just put the element
                # at the beginning of the list
                self.insert(0, node)

            else:
                for dependency in dependencies:
                    # if dependency is already in a list
                    if dependency not in self:
                        self.insert(len(self), dependency)

                # add the node the end of the list
                self.insert(len(self), node)
        else:
            # we can do something about this node only in the case it has
            # dependencies
            if dependencies:
                for dependency in dependencies:
                    if dependency not in self:
                        # add this dependency before the node
                        self.insert(self.index(node), dependency)
                    else:
                        # if dependency is already in the list, we need to
                        # make sure, that it's before the node
                        if self.index(dependency) > self.index(node):
                            # first, we're gonna remove that node from
                            # its old position
                            self.remove(node)
                            # and then insert it after the dependency
                            self.insert(self.index(dependency) + 1, node)


if __name__ == '__main__':
    pass
