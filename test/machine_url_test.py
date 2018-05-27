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
from machine.error import *


class TestMachineUrl(unittest.TestCase):

    def test_machine_url_fail_no_machine(self):
        try:
            url = manager.get_url("fake_machine")
            self.assertTrue(len(url) > 0)
        except MachineError as m:
            print("Successfully controlled url request on non existent machine")
            self.assertTrue(type(m) is MachineNoExistError)

    def test_machine_url_fail_machine_stopped(self):
        try:
            manager.create_default(autostart=True)
            manager.stop()
            url = manager.get_url()
            self.assertTrue(len(url) > 0)
        except MachineError as m:
            self.assertTrue(type(m) is MachineAlreadyStoppedError or type(m) is MachineStoppedError)

    def test_machine_url_success(self):
        try:
            manager.create_default(autostart=True)
            url = manager.get_url()
            print("Machine url is : "+url)
            self.assertTrue(len(url) > 0 and url.startswith("tcp://"))
        except MachineError as m:
            self.assertTrue(m is not None)


if __name__ == '__main__':
    unittest.main()
