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

import daemon
from loguru import logger

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
def process():
    pass


# Main function to run the daemon
def main():
    logger.add("service.log", rotation="1 day")

    # Check if the service is already running
    if is_service_running():
        logger.error("Another instance of the service is already running. Exiting.")
        return

    with daemon.DaemonContext():
        while True:
            try:
                logger.info("Processing unread blocks...")
                # process_unread_blocks()
                # logger.info("Processing complete. Sleeping for 1 hour.")
                time.sleep(3600)  # Sleep for 1 hour
            except Exception as e:
                logger.exception(f"An error occurred: {str(e)}")
                break

            # Remove the lock file to release the lock
            os.unlink(lock_file)


if __name__ == "__main__":
    main()
