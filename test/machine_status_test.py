import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError


class TestMachineStatus(unittest.TestCase):

    def test_machine_status_success(self):

        try:
            result = manager.status()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Default machine status is: "+result)
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
