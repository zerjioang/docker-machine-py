import unittest

from machine import get_machine, manager


class TestMachineCreate(unittest.TestCase):

    def test_machine_default_create(self):
        result = manager.create_default()
        print(result)
        self.assertTrue(result is not None)
        self.assertTrue(len(result) >= 1)


if __name__ == '__main__':
    unittest.main()
