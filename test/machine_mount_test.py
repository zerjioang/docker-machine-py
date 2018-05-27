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
from machine.error import MachineError, MachineNoExistError


class TestMachineMount(unittest.TestCase):

    def test_machine_mount_success(self):
        try:
            # todo: implement the test
            # manager.create_default(autostart=True)
            # result = manager.mount()
            self.assertTrue(False)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_unmount_success(self):
        try:
            # todo: implement the test
            # manager.create_default(autostart=True)
            # result = manager.mount()
            self.assertTrue(False)
        except MachineError as e:
            self.assertTrue(e is None)


if __name__ == '__main__':
    unittest.main()
