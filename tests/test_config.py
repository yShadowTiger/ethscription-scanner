# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
test_config.py

Feature:
    Unit test

Scenario:

"""
import unittest

from scanner.common import ConfigurationHelper


class ConfigTestCase(unittest.TestCase):

    def test_singleton(self):
        self.assertEqual(ConfigurationHelper(),
                         ConfigurationHelper())

    def test_get_config(self):
        internval = ConfigurationHelper().get_interval()
        self.assertEqual(3, internval)


if __name__ == '__main__':
    unittest.main()
