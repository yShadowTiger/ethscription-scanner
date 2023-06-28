# -*- coding: utf-8 -*-
# Author:   Alex Tang
# Date:     2023/6/28
"""
__main__.py

Feature:

Scenario:

"""
import fcntl
import os
import time

import click as click
import daemon
from loguru import logger

from scanner.chain import EthereumScanner
from scanner.common import ConfigurationHelper

lock_file = "/var/run/ethereum_service.lock"


# Check if the lock file exists
def is_service_running():
    try:
        with open(lock_file, "w") as f:
            fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as ioe:
        logger.error(ioe)
        return True
    return False


# Task processor
def execute():
    EthereumScanner().process()


# Main function to run the daemon
@click.command()
@click.option('-c', '--config', type=click.Path(exists=True), help='Config file path')
def main(config):
    logger.add("service.log", rotation="1 day", level="INFO")

    # Check if the service is already running
    if is_service_running():
        logger.error("Another instance of the service is already running. Exiting.")
        return

    with daemon.DaemonContext():
        while True:
            try:
                logger.info("Processing unread blocks...")
                execute()
                time.sleep(ConfigurationHelper().get_inteval())
            except Exception as e:
                logger.exception(f"An error occurred: {str(e)}")
                break

            # Remove the lock file to release the lock
            ConfigurationHelper().dump()
            os.unlink(lock_file)


if __name__ == "__main__":
    main()
