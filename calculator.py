import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Create entry widget to display the result
        self.result = tk.Entry(master, width=20, font=('Arial', 20, 'bold') )
        self.result.grid(row=0, column=0, columnspan=4, pady=30)

        # Create buttons for numbers 0-9 and operators
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '+', '=']
        ]

        for row in range(4):
            for col in range(4):
                button = tk.Button(master, text=buttons[row][col], width=5, height=3,
                                   font=('Arial', 14, 'bold'), command=lambda row=row, col=col: self.button_click(buttons[row][col]))
                button.grid(row=row+1, column=col, padx=5, pady=5)

        # Create a button to clear the entry widget
        clear_button = tk.Button(master, text='AC', width=5, height=2, font=('Arial', 14, 'bold'), bg='red', command=self.clear)
        clear_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

        # Create a button to delete the last character from the entry widget
        delete_button = tk.Button(master, text='DEL', width=5, height=2, font=('Arial', 14, 'bold'), command=self.delete)
        delete_button.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

    def button_click(self, value):
        current = self.result.get()  # Get the current content of the entry widget
        if value == '=':  # If the clicked button is the equals sign:
            try:
                result = eval(current)  # Evaluate the expression in the entry widget
                self.result.delete(0, tk.END)  # Clear the entry widget
                self.result.insert(0, result)  # Insert the result of the evaluation into the entry widget
            except:
                self.result.delete(0, tk.END)  # Clear the entry widget
                self.result.insert(0, 'Error')  # Display 'Error' in the entry widget
        else:  # If the clicked button is not the equals sign:
            self.result.delete(0, tk.END)  # Clear the entry widget
            self.result.insert(0, str(current) + str(value))  # Append the clicked button's value to the entry widget

    def clear(self):
        self.result.delete(0, tk.END)

    def delete(self):
        current = self.result.get()
        self.result.delete(0, tk.END)
        self.result.insert(0, current[:-1])


def main():
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()