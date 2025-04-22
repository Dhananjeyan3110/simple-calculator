import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()  
        # Create thgge input field
        self.input_text=tk.StringVar()
        self.input_field = tk.Entry(self,text=self.input_text, justify="right", width=30)
        self.input_field.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Create the buttons 
        buttons = [
            "7", "8", "9", "/", "sin",
            "4", "5", "6", "*", "cos",
            "1", "2", "3", "-", "tan",
            "0", ".", "=", "+", "sqrt",
        ]

        row = 1
        col = 0
        for button in buttons:
            button_action = lambda x=button: self.button_click(x)
            tk.Button(self, text=button, width=5, command=button_action).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Add memory buttons
        tk.Button(self, text="M+", width=5, command=self.memory_add).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self, text="M-", width=5, command=self.memory_subtract).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(self, text="MR", width=5, command=self.memory_recall).grid(row=5, column=2, padx=5, pady=5)
        tk.Button(self, text="MC", width=5, command=self.memory_clear).grid(row=5, column=3, padx=5, pady=5)

        # Add clear and delete buttons
        clear_button = tk.Button(self, text="C", width=5, command=self.clear_input)
        clear_button.grid(row=6, column=0, padx=5, pady=5)
        delete_button = tk.Button(self, text="DEL", width=5, command=self.delete_char)
        delete_button.grid(row=6, column=1, padx=5, pady=5)

        # Add history log
        self.history_text = tk.Text(self, width=25, height=5)
        self.history_text.grid(row=1, column=5, rowspan=5, padx=5, pady=5)

        # Bind the keyboard events to the calculator window
        self.bind("<Key>", self.keyboard_input)

        # Initialize memory
        self.memory = 0

    def button_click(self, button):
        # Handle button clicks
        if button == "=":
            try:
                result = eval(self.input_text.get())
                self.input_text.set(result)
                self.history_text.insert(tk.END, str(result) + "\n")
            except:
                self.input_text.set("ERROR")
        elif button == "sin":
            try:
                value = float(self.input_text.get())
                result = math.sin(value)
                self.input_text.set(result)
            except:
                self.input_text.set("ERROR")
        elif button == "cos":
            try:
                value = float(self.input_text.get())
                result = math.cos(value)
                self.input_text.set(result)
            except:
                self.input_text.set("ERROR")
        elif button == "tan":
            try:
                value = float(self.input_text.get())
                result = math.tan(value)
                self.input_text.set(result)
            except:
                self.input_text.set("ERROR")
        elif button == "sqrt":
            try:
                value = float(self.input_text.get())
                result = math.sqrt(value)
                self.input_text.set(result)
            except:
                self.input_text.set("ERROR")
        else:
            # Add the button text to the input field
            current_text = self.input_text.get()
            new_text = current_text + button
            self.input_text.set(new_text)

    def clear_input(self):
        # Clear the input field
        self.input_text.set("")

    def delete_char(self):
        # Delete the last character from the input field
        current_text = self.input_text.get()
        new_text = current_text[:-1]
        self.input_text.set(new_text)

    def keyboard_input(self, event):
        # Handle keyboard input
        if event.char in "0123456789+-*/.()":
            self.button_click(event.char)
        elif event.keysym == "Return":
            self.button_click("=")
        elif event.keysym == "BackSpace":
            self.delete_char()

    def memory_add(self):
        # Add the current input to memory
        current_input = self.input_text.get()
        try:
            current_input = float(current_input)
            self.memory += current_input
        except:
            pass

    def memory_subtract(self):
        # Subtract the current input from memory
        current_input = self.input_text.get()
        try:
            current_input = float(current_input)
            self.memory -= current_input
        except:
            pass

    def memory_recall(self):
        # Recall the value from memory and display it in the input field
        self.input_text.set(str(self.memory))

    def memory_clear(self):
        # Clear the value in memory
        self.memory = 0


calc = Calculator()
calc.mainloop()






