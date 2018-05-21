import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError


class TestMachineIP(unittest.TestCase):

    def test_machine_ip_success(self):
        try:
            manager.create_default(autostart=True)
            result = manager.ip()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine ip: " + str(result))
            '''
            example result
            192.168.99.100
            '''
            self.assertTrue(len(str(result).split("."))==4)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_env_fail(self):
        try:
            result = manager.ip("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled ip request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
