import customtkinter as ctk
from buttons import *

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Научный калькулятор")
        self.geometry("500x700")
        self.configure(fg_color="#FAFAFA")
        
        self.history = []
        self.expression = ""
        self.create_widgets()
        self.create_buttons()

    def create_widgets(self):
        self.history_frame = ctk.CTkFrame(self, height=80)
        self.history_frame.pack(pady=15, fill="x", padx=20)
        
        self.history_label = ctk.CTkLabel(
            self.history_frame, 
            text="История:",
            font=("Helvetica", 14),
            anchor="w"
        )
        self.history_label.pack(fill="x", padx=10)
        
        self.entry = ctk.CTkEntry(
            self,
            width=450,
            height=70,
            font=("Helvetica", 28),
            justify="right",
            fg_color="#FFFFFF",
            border_color="#BDBDBD"
        )
        self.entry.pack(pady=15)
        self.entry.insert(0, "0")

    def create_buttons(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack()

        scientific_frame = ctk.CTkFrame(main_frame)
        scientific_frame.pack(side="left", padx=5)
        
        for char in ["√", "%", "π", "e"]:
            ScientificButton(self, char).create_button(scientific_frame).pack(pady=2)

        button_layout = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('.', '0', '=', '+')
        ]
        
        buttons_frame = ctk.CTkFrame(main_frame)
        buttons_frame.pack(side="left")
        
        for row in button_layout:
            frame = ctk.CTkFrame(buttons_frame)
            frame.pack(pady=3)
            for char in row:
                if char in '1234567890.':
                    btn = DigitButton(self, char)
                elif char in '+-*/':
                    btn = OperationButton(self, char)
                elif char == '=':
                    btn = EqualsButton(self, char)
                btn.create_button(frame).pack(side="left", padx=3)

        control_frame = ctk.CTkFrame(self)
        control_frame.pack(pady=10)
        
        ClearButton(self, "C").create_button(control_frame).pack(side="left", padx=5)
        RandomNumberButton(self, "Rand").create_button(control_frame).pack(side="left", padx=5)
        ClearHistoryButton(self, "Очистить историю").create_button(control_frame).pack(side="left", padx=5)

    def update_display(self):
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, self.expression if self.expression else "0")

    def update_history(self):
        history_text = " | ".join(self.history[-3:])
        self.history_label.configure(text=history_text)