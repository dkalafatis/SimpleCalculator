import tkinter as tk
from tkinter import ttk


def on_click(character):
    """Handles button clicks, updating the display."""
    current_text = display.get()
    if current_text == "Error":
        display.set(character)
    else:
        display.set(current_text + character)


def evaluate():
    """Evaluates the expression in the display and shows the result."""
    try:
        result = eval(display.get())
        display.set(result)
    except Exception:
        display.set("Error")


def clear_display():
    """Clears the display."""
    display.set("")


# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Set a minimalistic design for the window
root.geometry("300x400")
root.resizable(False, False)

# StringVar to hold the display's content
display = tk.StringVar()

# Create the display area
display_entry = ttk.Entry(root, textvariable=display, font=("Arial", 16), justify="right")
display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Define button labels in a layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = ttk.Button(root, text=text, command=evaluate)
    elif text == 'C':
        btn = ttk.Button(root, text=text, command=clear_display)
    else:
        btn = ttk.Button(root, text=text, command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Make the grid cells expand evenly as the window size changes
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Start the Tkinter event loop
root.mainloop()
