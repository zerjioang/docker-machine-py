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

from machine import manager
from machine.error import MachineError, MachineNoExistError, MachineAlreadyRunningError


class TestMachineStart(unittest.TestCase):

    def test_machine_start_success(self):
        manager.create_default(autostart=False)
        result = manager.start()
        self.assertTrue(result is not None)
        self.assertTrue(len(result) >= 1)

    def test_machine_start_twice_success(self):
        """
        Test that tries to start the same machine twice
        :return:
        """
        try:
            manager.create_default()
            manager.start()
            result = manager.start()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            self.assertTrue(type(e) is MachineAlreadyRunningError)

    def test_machine_start_fail(self):
        """
        Test that tries to start a non existent machine
        :return:
        """
        try:
            result = manager.start("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled start request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
