import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to append a character to the display
def append_to_display(char):
    display.insert(tk.END, char)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display widget
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button configurations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them in the grid
for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), command=evaluate_expression)
        button.grid(row=row, column=column, sticky="nsew")
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: append_to_display(t))
        button.grid(row=row, column=column, sticky="nsew")

# Create clear button
clear_button = tk.Button(root, text="C", font=("Arial", 18), command=clear_display)
clear_button.grid(row=4, column=3, sticky="nsew")

# Make the buttons expand when the window is resized
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    if i < 4:
        root.grid_columnconfigure(i, weight=1)

# Bind the Enter key to evaluate the expression
root.bind('<Return>', evaluate_expression)

# Run the main event loop
root.mainloop()