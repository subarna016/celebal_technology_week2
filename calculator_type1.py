import tkinter as tk
from tkinter import font as tkfont

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator")

        # Set the font styles
        self.customFont = tkfont.Font(family="Comic Sans MS", size=16, weight="bold")
        self.buttonFont = tkfont.Font(family="Comic Sans MS", size=14)

        self.root.config(bg="#F5F5F5")

        self.display = tk.Entry(root, font=self.customFont, bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_data = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
        ]

        for (text, row, col) in button_data:
            self.create_button(text, row, col)

        self.create_button('C', 5, 0, 4)

    def create_button(self, text, row, col, colspan=1):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=self.buttonFont,
                           bg="#FFDDC1", fg="black", borderwidth=2, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text + char)


if __name__ == "__main__":
    root = tk.Tk()

    # Make the window size adjustable
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)

    app = CalculatorApp(root)
    root.mainloop()