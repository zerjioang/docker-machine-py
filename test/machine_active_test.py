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

import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError, MachineNoActiveHostError


class TestMachineActive(unittest.TestCase):

    '''
    a machine is considered active if the DOCKER_HOST environment variable points to it
    '''
    def test_machine_no_active_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.active()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine active list: "+result)
        except MachineError as e:
            self.assertTrue(type(e) is MachineNoActiveHostError)

    def test_machine_active_with_timeout_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.active(20)
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine active list: "+result)
        except MachineError as e:
            self.assertTrue(type(e) is MachineNoActiveHostError)


if __name__ == '__main__':
    unittest.main()
