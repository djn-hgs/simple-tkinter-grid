import tkinter as tk

root = tk.Tk()

# Let's create a grid of buttons...

rows = 3
columns = 3

buttons = {}

for i in range(rows):
    buttons[i] = {}
    for j in range(columns):
        # Create button

        buttons[i][j] = tk.Button(text=f'{(i,j)}')

        # Place on grid

        buttons[i][j].grid(row=i, column=j, sticky='news')

# Describe rows and columns

for row in range(rows):
    root.rowconfigure(row, weight=1)

for column in range(columns):
    root.columnconfigure(column, weight=1)

# Off we go

root.mainloop()
