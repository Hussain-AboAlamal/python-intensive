import logging
import os

LOG_FILE_NAME = os.getcwd() + os.sep + "log.txt"
DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(levelname)s %(asctime)s | %(filename)s | %(message)s"

LEVEL = os.environ.get("LOGLEVEL", DEFAULT_LOG_LEVEL)

# Config default logging
logging.basicConfig(filename=LOG_FILE_NAME, level=LEVEL, filemode='a', format=DEFAULT_LOG_FORMAT)


class SigletonMeta(type):
    
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyLogger(metaclass=SigletonMeta):
    
    def __init__(self) -> None:
        self.logger = logging.getLogger()

    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)
