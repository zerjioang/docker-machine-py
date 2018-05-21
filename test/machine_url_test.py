import unittest

from machine import manager
from machine.error import *


class TestMachineUrl(unittest.TestCase):

    def test_machine_url_fail_no_machine(self):
        try:
            url = manager.get_url("fake_machine")
            self.assertTrue(len(url) > 0)
        except MachineError as m:
            print("Successfully controlled url request on non existent machine")
            self.assertTrue(type(m) is MachineNoExistError)

    def test_machine_url_fail_machine_stopped(self):
        try:
            manager.stop()
            url = manager.get_url()
            self.assertTrue(len(url) > 0)
        except MachineError as m:
            self.assertTrue(type(m) is MachineAlreadyStoppedError)

    def test_machine_url_success(self):
        try:
            manager.create_default(autostart=True)
            url = manager.get_url()
            print("Machine url is : "+url)
            self.assertTrue(len(url) > 0)
        except MachineError as m:
            self.assertTrue(m is not None)


if __name__ == '__main__':
    unittest.main()
