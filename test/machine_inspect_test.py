import unittest

from machine import get_machine, manager
from machine.error import MachineError, MachineNoExistError


class TestMachineInspect(unittest.TestCase):

    def test_machine_inspect_success(self):
        try:
            manager.create_default(autostart=True)
            result = manager.inspect()
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
            print("Docker machine inspect: " + str(result))
            '''
            example result
            big json
            '''
            self.assertTrue(str(result).index('"ConfigVersion":') != -1)
            self.assertTrue(str(result).index('"EngineOptions": {') != -1)
            self.assertTrue(str(result).index('"SwarmOptions": {') != -1)
            self.assertTrue(str(result).index('"AuthOptions": {') != -1)
        except MachineError as e:
            self.assertTrue(e is None)

    def test_machine_inspect_fail(self):
        try:
            result = manager.inspect("fake_machine")
            self.assertTrue(result is not None)
            self.assertTrue(len(result) >= 1)
        except MachineError as e:
            print("Successfully controlled inspect request on non existent machine")
            self.assertTrue(type(e) is MachineNoExistError)


if __name__ == '__main__':
    unittest.main()
