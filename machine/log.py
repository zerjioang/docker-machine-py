"""
This file is part of docker-machine-py.

docker-machine-py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

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
