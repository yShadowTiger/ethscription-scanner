import signal
import time

from loguru import logger

from scanner.chain import EthereumScanner
from scanner.common import ConfigurationHelper

logger.add("service.log", rotation="1 day")


class SignalHandler:
    shutdown_requested = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.request_shutdown)
        signal.signal(signal.SIGTERM, self.request_shutdown)

    def request_shutdown(self, *args):
        logger.info('Request to shutdown received, stopping')
        self.shutdown_requested = True
        ConfigurationHelper().dump()

    def can_run(self):
        return not self.shutdown_requested


signal_handler = SignalHandler()

while signal_handler.can_run():
    EthereumScanner().process()
    logger.info("Processing complete. Sleeping for 1 minute.")
    time.sleep(ConfigurationHelper().get_interval())

logger.info("Shutting down, dump configuration")
