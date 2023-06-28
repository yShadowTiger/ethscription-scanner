# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
ConfigurationException.py

Feature:

Scenario:

"""


class ConfigurationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
