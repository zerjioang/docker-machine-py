from machine.machine import DockerMachine


def get_machine() -> DockerMachine:
    from machine.loader import DockerMachineInit
    init = DockerMachineInit()
    return init.find_machine()


manager = get_machine()
