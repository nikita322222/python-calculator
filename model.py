class CalculatorModel:
    def __init__(self):
        self.expression = "0"
        self.command_stack = []

    def append_to_expression(self, value):
        if self.expression == "0":
            self.expression = value
        else:
            self.expression += value

    def set_expression(self, value):
        self.expression = value

    def clear_expression(self):
        self.expression = "0"

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return True, result
        except Exception:
            self.expression = ""
            return False, "Ошибка"

    def get_expression(self):
        return self.expression if self.expression else "0"

    def push_command(self, command):
        self.command_stack.append(command)

    def undo_last_command(self):
        if self.command_stack:
            command = self.command_stack.pop()
            command.undo()
