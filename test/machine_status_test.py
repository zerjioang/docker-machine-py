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

from machine import get_machine, manager, DockerMachine
from machine.error import MachineError, MachineNoExistError


class TestMachineStatus(unittest.TestCase):

    def test_machine_status_running_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.status()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Default machine status is: "+result)
            self.assertTrue(result == DockerMachine.RUNNING)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_status_stop_success(self):

        try:
            manager.create_default(autostart=True)
            manager.stop()
            result = manager.status()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Default machine status is: "+result)
            self.assertTrue(result == DockerMachine.STOPPED)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_status_fail(self):
        try:
            result = manager.status("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled status request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
