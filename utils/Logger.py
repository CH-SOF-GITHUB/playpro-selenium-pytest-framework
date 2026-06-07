import logging

# define logging instance to log tests
logger = logging.getLogger(__name__)


class Logger:

    @staticmethod
    def set_message(message):
        logger.info(message)

"""
import logging

class Logger:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def set_message(self, message):
        self.logger.info(message)

Usage:
log = Logger()
log.set_message("Test passed")        
"""