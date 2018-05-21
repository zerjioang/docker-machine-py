import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError


class TestMachineActive(unittest.TestCase):

    def test_machine_active_success(self):

        try:
            manager.create_default(autostart=True)
            result = manager.active()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine active list: "+result)
        except MachineError as e:
            self.assertTrue(e is None)


if __name__ == '__main__':
    unittest.main()
