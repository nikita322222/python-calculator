import customtkinter as ctk
from abc import ABC, abstractmethod
from random import randint
import math

class Button(ABC):
    def __init__(self, calculator, char):
        self.calculator = calculator
        self.char = char
        self.width = 70
        self.height = 70
        self.font = ("Helvetica", 22, "bold")

    @abstractmethod
    def create_button(self, frame):
        pass

    @abstractmethod
    def on_click(self):
        pass

class DigitButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=self.width,
            height=self.height,
            font=self.font,
            fg_color="#E0E0E0",
            hover_color="#BDBDBD",
            text_color="#212121",
            command=self.on_click
        )

    def on_click(self):
        if self.calculator.expression == "0":
            self.calculator.expression = self.char
        else:
            self.calculator.expression += self.char
        self.calculator.update_display()

class OperationButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=self.width,
            height=self.height,
            font=self.font,
            fg_color="#78909C",
            hover_color="#546E7A",
            text_color="#FFFFFF",
            command=self.on_click
        )
    
    def on_click(self):
        if self.calculator.expression and self.calculator.expression[-1] not in '/*-+':
            self.calculator.expression += self.char
            self.calculator.update_display()

class EqualsButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=self.width,
            height=self.height,
            font=self.font,
            fg_color="#32CD32",
            hover_color="#228B22",
            command=self.on_click
        )

    def on_click(self):
        try:
            result = eval(self.calculator.expression)
            self.calculator.history.append(f"{self.calculator.expression} = {result}")
            if len(self.calculator.history) > 3:
                self.calculator.history.pop(0)
            self.calculator.expression = str(result)
            self.calculator.update_display()
            self.calculator.update_history()
        except:
            self.calculator.expression = ""
            self.calculator.entry.delete(0, ctk.END)
            self.calculator.entry.insert(0, "Ошибка")

class ScientificButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=self.width,
            height=40,
            font=("Helvetica", 16),
            fg_color="#78909C",
            hover_color="#546E7A",
            command=self.on_click
        )

    def on_click(self):
        try:
            # Обновляем выражение из entry, а не только из self.calculator.expression
            self.calculator.expression = self.calculator.entry.get()
            result = eval(self.calculator.expression)
            self.calculator.history.append(f"{self.calculator.expression} = {result}")
            if len(self.calculator.history) > 3:
                self.calculator.history.pop(0)
            self.calculator.expression = str(result)
            self.calculator.update_display()
            self.calculator.update_history()
        except:
            self.calculator.expression = ""
            self.calculator.entry.delete(0, ctk.END)
            self.calculator.entry.insert(0, "Ошибка")


    def _handle_result(self, operation, result):
        self.calculator.history.append(f"{operation}({self.calculator.expression}) = {result}")
        self.calculator.expression = str(result)
        self.calculator.update_display()
        self.calculator.update_history()

    def _show_error(self):
        self.calculator.expression = ""
        self.calculator.entry.delete(0, ctk.END)
        self.calculator.entry.insert(0, "Ошибка")

class ClearButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=140,
            height=40,
            font=("Helvetica", 16),
            fg_color="#FF5252",
            hover_color="#FF1744",
            command=self.on_click
        )
    
    def on_click(self):
        self.calculator.expression = ""
        self.calculator.update_display()

class ClearHistoryButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=140,
            height=40,
            font=("Helvetica", 16),
            fg_color="#FF7043",
            hover_color="#FF5722",
            command=self.on_click
        )
    
    def on_click(self):
        self.calculator.history = []
        self.calculator.update_history()

class RandomNumberButton(Button):
    def create_button(self, frame):
        return ctk.CTkButton(
            frame,
            text=self.char,
            width=140,
            height=40,
            font=("Helvetica", 16),
            fg_color="#AB47BC",
            hover_color="#9C27B0",
            command=self.on_click
        )
    
    def on_click(self):
        self.calculator.expression = str(randint(1, 1000))
        self.calculator.update_display()