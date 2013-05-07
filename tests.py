""" Test cases for the breadcrumbs module.
"""

import unittest
import breadcrumbs

class Class1(object):
    """ First class.
    """

    class_attr1 = "foo"

    def __init__(self):
        self.instance_attr1 = "foo"
        self.instance_attr2 = {
            "foo": "bar"
            }

    def foo(self):
        """ Foo!
        """
        return "bar"

    def bar(self, value):
        """ Bar!
        """
        return value

    @classmethod
    def foobar(cls, value):
        """ FooBar!
        """
        return value


class Class2(object):
    """ Other class.
    """

    def __init__(self):
        self.dict = {"foo": "bar"}
        self.instance = Class1()

    def __getitem__(self, item):
        return self.dict[item]

class TestCase(unittest.TestCase):
    """ Test the breadcrumbs module.
    """

    def test_getattr(self):
        """ Test for simple getattr.
        """
        instance1 = Class1()
        crumbs = breadcrumbs.root.instance_attr1
        self.assertEqual(breadcrumbs.collapse(crumbs, instance1), "foo")
        crumbs = breadcrumbs.root.class_attr1
        self.assertEqual(breadcrumbs.collapse(crumbs, instance1), "foo")

    def test_getitem(self):
        """ Test for simple getitem and getitem on an object.
        """
        dict1 = {"foo": "bar"}
        dict2 = Class2()
        crumbs = breadcrumbs.root["foo"]
        self.assertEqual(breadcrumbs.collapse(crumbs, dict1), "bar")
        self.assertEqual(breadcrumbs.collapse(crumbs, dict2), "bar")

    def test_call(self):
        """ Test calls with and without arguments.
        """
        instance = Class1()
        crumbs = breadcrumbs.root.foo()
        self.assertEqual(breadcrumbs.collapse(crumbs, instance), "bar")
        crumbs = breadcrumbs.root.bar("foo")
        self.assertEqual(breadcrumbs.collapse(crumbs, instance), "foo")

    def test_combine(self):
        """ Test combination of breadcrumbs.
        """
        instance1 = Class1()
        instance2 = Class2()
        crumbs = breadcrumbs.root.instance_attr2["foo"]
        self.assertEqual(breadcrumbs.collapse(crumbs, instance1), "bar")
        crumbs = breadcrumbs.root.instance.bar("foo")
        self.assertEqual(breadcrumbs.collapse(crumbs, instance2), "foo")
