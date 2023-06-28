# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
test_config.py

Feature:
    Unit test

Scenario:

"""
import os.path
import unittest

from loguru import logger

from scanner.common import ConfigurationHelper, Constant


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config_file_path = os.path.join(os.environ.get(Constant.KEY_PROJECT_DIRECTORY), 'scanner.conf')
        logger.info(self.config_file_path)

    def test_singleton(self):
        self.assertEqual(ConfigurationHelper(self.config_file_path),
                         ConfigurationHelper(self.config_file_path))

    def test_get_config(self):
        internval = ConfigurationHelper(self.config_file_path).get_interval()
        self.assertEqual(3, internval)


if __name__ == '__main__':
    unittest.main()
