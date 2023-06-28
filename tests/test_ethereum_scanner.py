# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
test_ethereum_scanner.py

Feature:
    Unit test

Scenario:

"""
import unittest

from scanner.chain import EthereumScanner


class EthereumScannerTestCase(unittest.TestCase):

    def setUp(self):
        self.scanner = EthereumScanner()

    def test_get_api_setting(self):
        self.assertIsNotNone(self.scanner)

    def test_process(self):
        self.scanner.process()
        self.assertIsNotNone(self.scanner)


if __name__ == '__main__':
    unittest.main()
