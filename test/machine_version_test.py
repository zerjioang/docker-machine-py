import unittest

from machine import manager


class TestGetVersion(unittest.TestCase):

    def test_machine_version(self):
        version = manager.get_version()
        print(version)
        self.assertTrue(str(version).startswith('docker-machine version '))


if __name__ == '__main__':
    unittest.main()
