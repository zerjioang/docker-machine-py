import unittest

from machine import manager


class TestGetVersion(unittest.TestCase):

    def test_machine_version(self):
        result = manager.get_help()
        self.assertEqual(len(result), 48)


if __name__ == '__main__':
    unittest.main()
