import logging

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class Log:

    def __init__(self, name):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('{}.log'.format(name))
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.log.addHandler(fh)
        self.log.addHandler(ch)

    def debug(self, msg):
        self.log.debug(str(msg))

    def info(self, msg):
        self.log.info(str(msg))

    def warning(self, msg):
        self.log.warning(str(msg))

    def critical(self, msg):
        self.log.critical(str(msg))

    def error(self, msg):
        self.log.error(str(msg))
