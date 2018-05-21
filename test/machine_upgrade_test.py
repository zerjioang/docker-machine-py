import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError


class TestMachineUpgrade(unittest.TestCase):

    def test_machine_upgrade_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.upgrade()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_upgrade_fail(self):
        try:
            result = manager.upgrade("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled upgrade request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
