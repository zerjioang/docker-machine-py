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
