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
from machine.utils import find_file


class DockerMachineInit(LogObject):

    def __init__(self):
        super().__init__()
        self.logger.debug("Initializing docker-machine...")
        self.default_location = "/usr/local/bin/docker-machine"
        self.machine_location = self.default_location
        self.name = "docker-machine"
        self.machine = None

    def find_machine(self):
        from machine import DockerMachine
        self.logger.debug("Finding docker machine in current system...")
        self.machine_location = find_file(self.name)
        self.logger.debug("docker-machine found in: "+str(self.machine_location))
        self.machine = DockerMachine(self.machine_location)
        return self.machine
