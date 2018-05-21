from machine.log import LogObject


class MachineError(BaseException):

    def __init__(self, message: list):
        self.logger = LogObject()
        if len(message) == 1:
            self.message = message[0]
        else:
            self.message = message
        self.logger.logger.error(self.message)


class MachineStoppedError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyExistError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyRunningError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineNoExistError(MachineError):

    def __init__(self, message: list):
        self.message = message


class MachineAlreadyStoppedError(MachineError):

    def __init__(self, message: list):
        self.message = message