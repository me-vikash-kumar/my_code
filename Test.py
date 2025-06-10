import tkinter as tk
from tkinter import messagebox, simpledialog
import sys

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')
        
        # Create main interface
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🧮 Simple Calculator", 
            font=("Arial", 18, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # Instructions
        instruction_label = tk.Label(
            self.root,
            text="Choose an operation:",
            font=("Arial", 12),
            bg='#f0f0f0',
            fg='#666666'
        )
        instruction_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Operation buttons
        buttons = [
            ("➕ Addition", self.perform_addition, '#4CAF50'),
            ("➖ Subtraction", self.perform_subtraction, '#FF9800'),
            ("✖️ Multiplication", self.perform_multiplication, '#2196F3'),
            ("➗ Division", self.perform_division, '#9C27B0'),
            ("🚪 Exit", self.exit_app, '#f44336')
        ]
        
        for i, (text, command, color) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 11, "bold"),
                bg=color,
                fg='white',
                width=20,
                height=2,
                relief='raised',
                bd=2
            )
            btn.pack(pady=5)
    
    def get_numbers(self, operation_name):
        """Get two numbers from user input dialogs"""
        try:
            a = simpledialog.askfloat(
                f"{operation_name} - Input",
                "Enter the first number:",
                parent=self.root
            )
            if a is None:  # User cancelled
                return None, None
                
            b = simpledialog.askfloat(
                f"{operation_name} - Input",
                "Enter the second number:",
                parent=self.root
            )
            if b is None:  # User cancelled
                return None, None
                
            return a, b
        except:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return None, None
    
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            return None  # Handle division by zero
        return a / b
    
    def perform_addition(self):
        a, b = self.get_numbers("Addition")
        if a is not None and b is not None:
            result = self.addition(a, b)
            messagebox.showinfo(
                "Addition Result", 
                f"{a} + {b} = {result}"
            )
    
    def perform_subtraction(self):
        a, b = self.get_numbers("Subtraction")
        if a is not None and b is not None:
            result = self.subtraction(a, b)
            messagebox.showinfo(
                "Subtraction Result", 
                f"{a} - {b} = {result}"
            )
    
    def perform_multiplication(self):
        a, b = self.get_numbers("Multiplication")
        if a is not None and b is not None:
            result = self.multiplication(a, b)
            messagebox.showinfo(
                "Multiplication Result", 
                f"{a} × {b} = {result}"
            )
    
    def perform_division(self):
        a, b = self.get_numbers("Division")
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror(
                    "Division Error", 
                    "Cannot divide by zero!\nPlease provide a valid denominator."
                )
            else:
                result = self.division(a, b)
                messagebox.showinfo(
                    "Division Result", 
                    f"{a} ÷ {b} = {result}"
                )
    
    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()
            sys.exit()
    
    def run(self):
        # Center the window on screen
        self.root.eval('tk::PlaceWindow . center')
        self.root.mainloop()

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()