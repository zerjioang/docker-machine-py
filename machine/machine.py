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

from machine.error import MachineError, MachineAlreadyExistError, MachineStoppedError, MachineNoExistError, \
    MachineInvalidCertsError
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

    def active(self, timeout=10):
        # evaluate user specified timeout value
        if timeout >= 0:
            t = timeout
        else:
            t = 10
        data = self.docker_machine_exec(
            ["active", "--timeout", str(t)])
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

    def env(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            try:
                data = self.docker_machine_exec(["env",machine])
            except MachineInvalidCertsError as e:
                self.regenerate_certs(machine)
                # try again
                data = self.docker_machine_exec(["env", machine])
            if data is not None:
                return data
        return None

    def inspect(self, machine=DEFAULT_MACHINE_NAME, inspect_format=""):
        if self.is_valid_machine_name(machine):
            params = "inspect"
            if inspect_format is not None and len(inspect_format) > 0:
                params += "--format " + inspect_format

            data = self.docker_machine_exec(
                [
                    params,
                    machine
                ])

            if data is not None:
                return data
        return None

    def ip(self, machine=DEFAULT_MACHINE_NAME) -> str:
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "ip",
                    machine
                ])
            if data is not None and len(data) == 1:
                return data[0]
        return None

    def kill(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "kill",
                    machine
                ])
            if data is not None:
                return data
        return None

    def list(self, quiet=False, filters="", timeout=0, list_format=""):
        params = "ls"
        if quiet:
            # Enable quiet mode
            params += " --quiet"
        if filters is not None and len(filters) > 0:
            params += "--filter " + filters
        if timeout is not None and timeout > 0:
            params += "--timeout " + str(timeout)
        if list_format is not None and len(list_format) > 0:
            params += "--format " + list_format
        data = self.docker_machine_exec([params])
        if data is not None:
            return data
        return None

    def provision(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "provision",
                    machine
                ])
            if data is not None:
                return data
        return None

    def regenerate_certs(self, name=DEFAULT_MACHINE_NAME, force=True, client_certs=False):
        cmd = ["regenerate-certs"]
        if force:
            # Force rebuild and do not prompt
            cmd.append("--force")
        if client_certs:
            # Also regenerate client certificates and CA.
            cmd.append("--client-certs")
        cmd.append(name)
        data = self.docker_machine_exec(cmd)
        if data is not None:
            return data
        return None

    def restart(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "restart",
                    machine
                ])
            if data is not None:
                return data
        return None

    def remove(self, machine=DEFAULT_MACHINE_NAME, force=True, yes=True):
        if self.is_valid_machine_name(machine):
            params = "rm"
            if force:
                # Remove local configuration even if machine cannot be removed, also implies an automatic yes
                params += " --force"
            if yes:
                # Assumes automatic yes to proceed with remove, without prompting further user confirmation
                params += " -y"
            data = self.docker_machine_exec(
                [
                    params,
                    machine
                ])
            if data is not None:
                return data
        return None

    def ssh(self, machine=DEFAULT_MACHINE_NAME, command=""):
        if self.is_valid_machine_name(machine):
            if command is None:
                command = ""

            data = self.docker_machine_exec(
                [
                    "ssh",
                    machine,
                    command
                ])

            if data is not None:
                return data
        return None

    def scp(self, user="", machine=DEFAULT_MACHINE_NAME, path="", target_user="", target_machine="", target_path="",
            recursive=True, delta=False, quiet=True):
        params = "scp"
        # configure scp params
        params += user + "@" + machine + ":" + path + " " + target_user + "@" + target_machine + ":" + target_path
        # configure command options
        if recursive:
            params += " --recursive"
        if delta:
            params += " --delta"
        if quiet:
            params += " --quiet"
        data = self.docker_machine_exec(
            [
                params
            ])
        if data is not None:
            return data
        return None

    def mount(self, machine=DEFAULT_MACHINE_NAME, path=None, mount_point=None, unmount=False):
        # check params
        valid = machine is not None and path is not None and mount_point is not None
        if valid:
            params = machine + ":" + path + " " + mount_point
            cmd = ["mount", params]
            if unmount:
                cmd = ["mount", "--unmount", params]

            data = self.docker_machine_exec(
                cmd)
            if data is not None:
                return data
        return None

    def start(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "start",
                    machine
                ])
            if data is not None:
                return data
        return None

    def status(self, machine=DEFAULT_MACHINE_NAME) -> str:
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "status",
                    machine
                ])
            if data is not None and len(data) == 1:
                return data[0]
        return ""

    def stop(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "stop",
                    machine
                ])
            if data is not None:
                return data
        return None

    def upgrade(self, machine=DEFAULT_MACHINE_NAME):
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "upgrade",
                    machine
                ])
            if data is not None:
                return data
        return None

    def get_url(self, machine=DEFAULT_MACHINE_NAME) -> str:
        if self.is_valid_machine_name(machine):
            data = self.docker_machine_exec(
                [
                    "url",
                    machine
                ])
            if data is not None and len(data) == 1:
                return data[0]
        return ""

    def get_version(self) -> str:
        data = self.docker_machine_exec(
            [
                "version"
            ])
        if data is not None:
            return data[0]
        return ""

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

    def create_amazon(self, config: EC2MachineConfig):
        # docker-machine create --driver amazonec2 -h
        cmd = ["create", "--driver", "amazonec2", config.asList()]
        data = self.docker_machine_exec(cmd)
        if data is not None:
            return data
        return None

    def create_azure(self, config: AzureMachineConfig):
        # docker-machine create --driver amazonec2 -h
        cmd = ["create", "--driver", "amazonec2", config.asList()]
        data = self.docker_machine_exec(cmd)
        if data is not None:
            return data
        return None

    def exists(self, name=DEFAULT_MACHINE_NAME) -> bool:
        if self.is_valid_machine_name(name):
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
        return False

    def is_valid_machine_name(self, name: str):
        return name is not None and len(name.rstrip()) > 0
