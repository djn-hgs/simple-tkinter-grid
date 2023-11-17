import tkinter as tk

root = tk.Tk()


# A button to print something

class button_that_prints(tk.Button):
    def __init__(self, row, column):
        super().__init__()
        self.row = row
        self.column = column

    def clicked(self):
        print(f"You clicked a button {(self.row, self.column)}... but I don't know which one.")

def print_something():
    print('Bang')

# Let's create a grid of buttons...

rows = 8
columns = 8

buttons = {}

for i in range(rows):
    buttons[i] = {}
    for j in range(columns):
        # Create button

        new_button = button_that_prints(row=i, column=j)

        new_button.configure(command=new_button.clicked)

        buttons[i][j] = new_button

        # Place on grid

        buttons[i][j].grid(row=i, column=j, sticky='news')

# Describe rows and columns

for row in range(rows):
    root.rowconfigure(row, weight=1)

for column in range(columns):
    root.columnconfigure(column, weight=1)

# Off we go

root.mainloop()
