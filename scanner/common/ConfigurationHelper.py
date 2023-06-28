# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
ConfigurationHelper.py

Feature:

Scenario:

"""
import configparser
import os.path

from scanner.common import ConfigurationException


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class ConfigurationHelper:

    def __init__(self, file_path):
        self.config_file_path = file_path
        self.config = configparser.ConfigParser()
        if os.path.exists(self.config_file_path):
            self.config.read(file_path)
        else:
            raise ConfigurationException(f'Config file {file_path} not found')

    def get_interval(self):
        return self.config.getint('scanner', 'interval')

    def get_last_block(self):
        return self.config.getint('scanner', 'last_block')

    def set_last_block(self, last_block):
        self.config.setint('scanner', 'LastBlock', str(last_block))
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)
