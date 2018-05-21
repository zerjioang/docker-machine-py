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

from machine.error import MachineError, MachineAlreadyExistError, MachineStoppedError, MachineNoExistError
from machine.loader import LogObject
from machine.utils import execute_command


class DockerMachine(LogObject):
    
    URL_ID = "tcp://"
    RUNNING = "Running"
    STOPPED = "Stopped"
    DEFAULT_MACHINE_NAME = "default"

    def __init__(self, location: str):
        super().__init__()
        self.docker_machine_exec_path = location

    def docker_machine_exec(self, params: list) -> list:
        log_lines = execute_command(
            self.docker_machine_exec_path,
            params
        )
        if log_lines is not None and len(log_lines) > 0:
            for l in log_lines:
                print(l)
            return log_lines

    def active(self):
        data = self.docker_machine_exec(["active"])
        if data is not None:
            return data
        return None

    def config(self, name=DEFAULT_MACHINE_NAME, swarm_config=False):
        cmd = ["config", name]
        if swarm_config:
            cmd = ["config", "--swarm", name]
        data = self.docker_machine_exec(cmd)
        if data is not None:
            return data
        return None

    def create(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "create",
                name
            ])
        if data is not None:
            return data
        return None

    def env(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "env",
                name
            ])
        if data is not None:
            return data
        return None

    def inspect(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "inspect",
                name
            ])
        if data is not None:
            return data
        return None

    def ip(self, name=DEFAULT_MACHINE_NAME) -> str:
        data = self.docker_machine_exec(
            [
                "ip",
                name
            ])
        if data is not None and len(data) == 1:
            return data[0]
        return None

    def kill(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "kill",
                name
            ])
        if data is not None:
            return data
        return None

    def list(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "ls",
                name
            ])
        if data is not None:
            return data
        return None

    def provision(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "provision",
                name
            ])
        if data is not None:
            return data
        return None

    def regnerate_certs(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "regenerate-certs",
                name
            ])
        if data is not None:
            return data
        return None

    def restart(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "restart",
                name
            ])
        if data is not None:
            return data
        return None

    def remove(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "rm",
                name
            ])
        if data is not None:
            return data
        return None

    def ssh(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "ssh",
                name
            ])
        if data is not None:
            return data
        return None

    def csp(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "scp",
                name
            ])
        if data is not None:
            return data
        return None

    def mount(self, name=DEFAULT_MACHINE_NAME, unmount=False):
        cmd = ["mount", name]
        if unmount:
            cmd = ["mount", "--unmount", name]

        data = self.docker_machine_exec(
            cmd)
        if data is not None:
            return data
        return None

    def start(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "start",
                name
            ])
        if data is not None:
            return data
        return None

    def status(self, name=DEFAULT_MACHINE_NAME) -> str:
        data = self.docker_machine_exec(
            [
                "status",
                name
            ])
        if data is not None and len(data) == 1:
            return data[0]
        return None

    def stop(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "stop",
                name
            ])
        if data is not None:
            return data

    def upgrade(self, name=DEFAULT_MACHINE_NAME):
        data = self.docker_machine_exec(
            [
                "upgrade",
                name
            ])
        if data is not None:
            return data
        return None

    def get_url(self, machine_id=DEFAULT_MACHINE_NAME) -> str:
        data = self.docker_machine_exec(
            [
                "url",
                machine_id
            ])
        if data is not None and len(data) == 1:
            return data[0]
        return None

    def get_version(self):
        data = self.docker_machine_exec(
            [
                "version"
            ])
        if data is not None:
            return data[0]
        return None

    def get_help(self):
        data = self.docker_machine_exec(
            [
                "help"
            ])
        if data is not None:
            return data
        return None

    # helper methods. must be exception safe.

    def create_default(self, autostart=False) -> list:
        if not self.exists():
            try:
                self.create()
            except MachineError as e:
                return [e.message]
        if autostart:
            if self.status() == DockerMachine.STOPPED:
                return self.start()

    def exists(self, name=DEFAULT_MACHINE_NAME) -> bool:
        try:
            data = self.get_url(name)
            # example: tcp://192.168.99.100:2376
            return len(data) > 0 and data.startswith(DockerMachine.URL_ID)
        except MachineStoppedError:
            return True
        except MachineAlreadyExistError:
            return True
        except MachineNoExistError:
            return False
