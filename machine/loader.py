from machine.log import LogObject
from machine.utils import find_file


class DockerMachineInit(LogObject):

    def __init__(self):
        super().__init__()
        self.logger.debug("Initializing docker-machine...")
        self.default_location = "/usr/local/bin/docker-machine"
        self.machine_location = self.default_location
        self.name = "docker-machine"
        self.machine = None

    def find_machine(self):
        from machine import DockerMachine
        self.logger.debug("Finding docker machine in current system...")
        self.machine_location = find_file(self.name)
        self.logger.debug("docker-machine found in: "+str(self.machine_location))
        self.machine = DockerMachine(self.machine_location)
        return self.machine
