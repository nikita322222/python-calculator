import customtkinter as ctk
from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self, controller, char):
        self.controller = controller
        self.char = char

    @abstractmethod
    def create_button(self, frame):
        pass

    @abstractmethod
    def on_click(self):
        pass

class DigitButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(frame, text=self.char, width=60, height=60, font=("Arial", 20), command=self.on_click)

    def on_click(self):
        self.controller.append_to_expression(self.char)

class OperationButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(frame, text=self.char, width=60, height=60, font=("Arial", 20),
                             fg_color="#808080", hover_color="#5D5D5D", command=self.on_click)

    def on_click(self):
        self.controller.append_to_expression(self.char)

class EqualsButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(frame, text=self.char, width=60, height=60, font=("Arial", 20),
                             fg_color="#32CD32", hover_color="#228B22", command=self.on_click)

    def on_click(self):
        self.controller.evaluate_expression()

class ClearButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(frame, text=self.char, width=280, height=40, font=("Arial", 16, "bold"),
                             fg_color="#FF0000", hover_color="#CC0000", command=self.on_click)

    def on_click(self):
        self.controller.clear_expression()
