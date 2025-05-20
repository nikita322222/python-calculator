from model import CalculatorModel
from view import CalculatorView
from command import AppendCommand, ClearCommand, EvaluateCommand

class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self)

    def run(self):
        self.view.mainloop()

    def append_to_expression(self, value):
        command = AppendCommand(self.model, value)
        command.execute()
        self.model.push_command(command)
        self.view.update_display(self.model.get_expression())

    def set_expression(self, value):
        self.model.set_expression(value)
        self.view.update_display(self.model.get_expression())

    def clear_expression(self):
        command = ClearCommand(self.model)
        command.execute()
        self.model.push_command(command)
        self.view.update_display(self.model.get_expression())

    def evaluate_expression(self):
        command = EvaluateCommand(self.model)
        command.execute()
        self.model.push_command(command)
        self.view.update_display(str(command.result))

    def undo(self):
        self.model.undo_last_command()
        self.view.update_display(self.model.get_expression())
