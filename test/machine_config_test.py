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


class TestMachineConfig(unittest.TestCase):

    def test_machine_config_success(self):
        try:
            manager.create_default(autostart=True)
            result = manager.config()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine configuration: " + str(result))
            values = ['--tlsverify', '--tlscacert=', '--tlscert=', '--tlskey=', '-H=tcp://']
            for i in range(len(result)-1):
                line = str(result[i])
                match = values[i]
                print(line+" "+match)
                self.assertTrue(line.startswith(match))
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_config_swarm_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.config(swarm_config=True)
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine swarm configuration: " + str(result))
            self.assertTrue(False)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_config_fail(self):
        try:
            result = manager.config("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled config request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)

    def test_machine_config_swarm_fail(self):
        try:
            result = manager.config("fake_machine", swarm_config=True)
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled swarm config request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
