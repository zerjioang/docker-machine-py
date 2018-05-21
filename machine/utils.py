"""
This file is part of docker-machine-py.

docker-machine-py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import subprocess

from machine.error import *


def is_exe(f):
    if f is not None:
        return os.path.isfile(f) and os.access(f, os.X_OK)
    return False


def parse_result(stdout):
    output = stdout.decode()
    data = output.split('\n')
    if len(data) == 2 and data[1] is '':
        return [data[0]]
    else:
        return data


def execute_command(executable: str, commands: list) -> list:
    commands.insert(0, executable)
    p = subprocess.Popen(commands,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    error_code = p.returncode
    if error_code == 0:
        return parse_result(stdout)
    else:
        '''
        Known errors: virtual box not installed:
        wget -q -O - http://download.virtualbox.org/virtualbox/debian/oracle_vbox_2016.asc | sudo apt-key add -
        sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian bionic non-free contrib"
        >> /etc/apt/sources.list.d/virtualbox.org.list' 
        apt install virtualbox
        '''
        error = parse_result(stderr)
        if len(error) == 1:
            msg = error[0]
            if msg == "Host is not running":
                raise MachineStoppedError(msg)
            elif msg.startswith('Docker machine "') and msg.endswith('to add a new one.'):
                raise MachineNoExistError(msg)
            elif msg.startswith('Docker machine "') and msg.endswith('" already exists'):
                raise MachineAlreadyExistError(msg)
            elif msg.endswith('" is already running.'):
                raise MachineAlreadyRunningError(msg)
            elif msg.endswith('" is already stopped.'):
                raise MachineAlreadyStoppedError(msg)
            else:
                raise MachineError(msg)
        else:
            raise MachineError(error)


def find_file(file_name):
    result = execute_command('whereis', [file_name])[0]
    if result is not None:
        return result.split(":")[1].strip()


def which(program: str):
    """
    Find requested program in system path
    Args:
        program (str): the program name to be found
    Returns:
        if found the full path to the program, else None
    """

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None


def freeze_port_binding():
    """
    sudo netstat -pan | grep 41463
    and then kill process based on pid
    :return:
    """
    pass
