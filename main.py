import tkinter as tk

root = tk.Tk()


# This is a button that knows how to print something
# It is just a tkinter Button which we then add extra bits to
# The (tk.Button) line says we are inheriting from the tkinter class

class ButtonThatPrints(tk.Button):

    # Our __init__ has parameters for the button's row and column
    # I've kept it simple, so any config will have to be done via "configure"
    # (See later code)
    def __init__(self, button_row, button_column):

        # super() is the button's parent class - in this case tk.Button
        # It needs to grab all the initialisation that a standard button would have

        super().__init__()

        # Store the row and column in the button's properties

        self.row = button_row
        self.column = button_column

    # This is the button's own, personal "clicked" method

    def clicked(self):
        print(f"You clicked button {(self.row, self.column)}.")

# We don't need this any more
#
#def print_something():
#    print('Bang')


# Let's create a grid of buttons...

# I used variables to prove that the grid can have any size

rows = 8
columns = 8

# Showing off by storing the buttons in a dictionary of dictionaries
# (why not? it's fun)

# The rows
buttons = {}

for i in range(rows):

    # The cells in each row
    buttons[i] = {}

    for j in range(columns):
        # Create button and pass through its location

        new_button = ButtonThatPrints(button_row=i, button_column=j)

        # We then pass the button's own ButtonThatPrints.clicked() method as its own comman
        new_button.configure(command=new_button.clicked)

        # (We can only do this once the button exists

        # Store the button in my dictionary of dictionaries

        buttons[i][j] = new_button

        # Place on grid and let it fill its entry

        buttons[i][j].grid(row=i, column=j, sticky='news')

# Describe rows and columns - these will fill the screen

for row in range(rows):
    root.rowconfigure(row, weight=1)

for column in range(columns):
    root.columnconfigure(column, weight=1)

# Off we go

root.mainloop()
