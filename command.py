from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AppendCommand(Command):
    def __init__(self, model, value):
        self.model = model
        self.value = value
        self.prev_expression = model.get_expression()

    def execute(self):
        self.model.append_to_expression(self.value)

    def undo(self):
        self.model.set_expression(self.prev_expression)


class ClearCommand(Command):
    def __init__(self, model):
        self.model = model
        self.prev_expression = model.get_expression()

    def execute(self):
        self.model.clear_expression()

    def undo(self):
        self.model.set_expression(self.prev_expression)


class EvaluateCommand(Command):
    def __init__(self, model):
        self.model = model
        self.prev_expression = model.get_expression()
        self.result = None

    def execute(self):
        success, result = self.model.evaluate_expression()
        self.result = result

    def undo(self):
        self.model.set_expression(self.prev_expression)
