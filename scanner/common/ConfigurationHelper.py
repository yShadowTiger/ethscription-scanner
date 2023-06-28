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

from scanner.common import ConfigurationException, Constant


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class ConfigurationHelper:

    def __init__(self):
        self.config_file_path = os.path.join(os.environ.get(Constant.KEY_PROJECT_DIRECTORY),
                                             Constant.PROJECT_CONFIG_FILE)
        self.config = configparser.ConfigParser()
        if os.path.exists(self.config_file_path):
            self.config.read(self.config_file_path)
        else:
            raise ConfigurationException(f'Config file {self.config_file_path} not found')

        self.interval = self.config.getint('scanner', 'interval')
        self.last_block = self.config.getint('scanner', 'last_block')

    def get_interval(self):
        return self.interval

    def get_last_block(self):
        return self.last_block

    def set_last_block(self, last_block):
        self.last_block = last_block

    def dump(self, last_block):
        self.config.setint('scanner', 'last_block', str(last_block))
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)
