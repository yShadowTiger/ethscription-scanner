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


class EthereumScanner(EVMScanner):
    KEY_API_SETTING = 'ETHEREUM_API'

    def __init__(self):
        super().__init__()

    def process(self):
        latest_block_number = self.get_latest_block_number()

        for offset in range(100, 10, -1):
            block_number = latest_block_number - offset
            block = self.get_block(block_number)
            self.parse_block(block)

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
