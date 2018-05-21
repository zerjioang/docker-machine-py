import coloredlogs
import logging


class LogObject(object):

    def __init__(self):
        # Create a logger object.
        self.logger = logging.getLogger(__name__)

        # If you don't want to see log messages from libraries, you can pass a
        # specific logger object to the install() function. In this case only log
        # messages originating from that logger will show up on the terminal.
        coloredlogs.install(level='DEBUG', logger=self.logger, milliseconds=True)
