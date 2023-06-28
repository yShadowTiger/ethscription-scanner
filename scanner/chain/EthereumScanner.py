# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
EthereumScanner.py

Feature:

Scenario:

"""
from loguru import logger

from scanner.chain import EVMScanner
from scanner.common import ConfigurationHelper


class EthereumScanner(EVMScanner):
    KEY_API_SETTING = 'ETHEREUM_API'
    MAX_BLOCKS = 1000

    def __init__(self):
        super().__init__()

    def process(self):
        last_block_numer = ConfigurationHelper().get_last_block()
        latest_block_number = self.get_latest_block_number()

        if latest_block_number > last_block_numer + self.MAX_BLOCKS:
            latest_block_number = last_block_numer + self.MAX_BLOCKS

        for block_number in range(last_block_numer, latest_block_number):
            block = self.get_block(block_number)
            self.parse_block(block)
            ConfigurationHelper().set_last_block(block_number)

    def get_latest_block_number(self):
        latest_block_number = self.web3.eth.block_number
        logger.debug(f"Latest block number: {latest_block_number}")
        return latest_block_number

    def get_block(self, block_number):
        block = self.web3.eth.get_block(block_number, full_transactions=True)
        logger.debug(f"Block number: {block_number}")
        logger.debug(f"Transactions: {len(block['transactions'])}")
        return block

    def parse_block(self, block):
        for tx in block['transactions']:
            data = tx['input']
            binary_data = bytes.fromhex(data[2:])
            if binary_data.startswith(b"data:"):
                logger.info(str(binary_data, 'utf-8'))
