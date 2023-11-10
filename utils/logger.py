import logging
import sys


def custom_logger(log_level=logging.INFO):
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        stream=sys.stdout
    )
    logger = logging.getLogger(__name__)
    return logger
