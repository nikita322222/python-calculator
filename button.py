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

# Декоратор с подсветкой кнопки при наведении
class ButtonDecorator(Button):
    def __init__(self, button: Button):
        self._button = button
        self.controller = button.controller
        self.char = button.char
        self._btn_widget = None

    def create_button(self, frame):
        # создаём оригинальную кнопку
        btn = self._button.create_button(frame)
        self._btn_widget = btn

        # Цвета для подсветки
        self._normal_color = btn.cget("fg_color") or btn.cget("bg") or "#FFFFFF"
        self._hover_color = "#FFD700"  # золотистый для подсветки

        # Привязываем события наведения
        btn.bind("<Enter>", self._on_enter)
        btn.bind("<Leave>", self._on_leave)
        return btn

    def _on_enter(self, event):
        # Меняем цвет фона кнопки при наведении
        if isinstance(self._btn_widget, ctk.CTkButton):
            self._btn_widget.configure(fg_color=self._hover_color)

    def _on_leave(self, event):
        # Возвращаем исходный цвет
        if isinstance(self._btn_widget, ctk.CTkButton):
            self._btn_widget.configure(fg_color=self._normal_color)

    def on_click(self):
        print(f"Button '{self.char}' clicked")
        self._button.on_click()
