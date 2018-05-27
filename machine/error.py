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
from machine.log import LogObject


class MachineError(BaseException):

    def __init__(self, message: list):
        self.logger = LogObject()
        if len(message) == 1:
            self.message = message[0]
        else:
            self.message = message
        self.logger.logger.error(self.message)


class MachineStoppedError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyExistError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyRunningError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineNoExistError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyStoppedError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineNoActiveHostError(MachineError):

    def __init__(self, message: list):
        self.message = message

class MachineInvalidCertsError(MachineError):

    def __init__(self, message: list):
        self.message = message

