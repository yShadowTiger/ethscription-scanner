# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
EVMScanner.py

Feature:

Scenario:

"""
import os
from abc import ABC, abstractmethod

from web3 import Web3

from scanner.common import ConfigurationException


class EVMScanner(ABC):
    KEY_API_SETTING = 'EVM_API'

    def __init__(self):
        self.api_setting = os.environ.get(self.KEY_API_SETTING)
        if self.api_setting is None:
            raise ConfigurationException('EVM API setting is not configured')
        self.web3 = Web3(Web3.HTTPProvider(self.api_setting))

    @abstractmethod
    def process(self):
        pass
