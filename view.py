import customtkinter as ctk
from button import DigitButton, OperationButton, EqualsButton, ClearButton, ButtonDecorator
import platform

class CalculatorView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Калькулятор")
        self.geometry("350x500")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_widgets()
        self.create_buttons()
        self.bind_hotkeys()

    def create_widgets(self):
        self.entry = ctk.CTkEntry(self, width=280, height=50, font=("Arial", 24), justify="right")
        self.entry.pack(pady=10)
        self.entry.insert(0, "0")

    def create_buttons(self):
        button_layout = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in button_layout:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=2)
            for char in row:
                if char.isdigit() or char == '.':
                    button = DigitButton(self.controller, char)
                elif char in '/*-+':
                    button = OperationButton(self.controller, char)
                elif char == '=':
                    button = EqualsButton(self.controller, char)

                decorated_button = ButtonDecorator(button)

                btn = decorated_button.create_button(frame)
                btn.pack(side="left", padx=5)

        clear_button = ClearButton(self.controller, "Очистить")
        decorated_clear = ButtonDecorator(clear_button)
        decorated_clear.create_button(self).pack(pady=10)

    def update_display(self, text):
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, text)

    def bind_hotkeys(self):
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            self.bind_all("<Command-z>", lambda e: self.controller.undo())
        else:
            self.bind_all("<Control-z>", lambda e: self.controller.undo())
