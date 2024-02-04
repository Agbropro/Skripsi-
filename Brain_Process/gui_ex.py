import tkinter as tk
from tkinter import messagebox

def show_custom_size_message():
    messagebox.showinfo("Custom Size", "This is a messagebox with custom size.")
    # Set custom size for the messagebox
    root.geometry("600x300")

# Create the main window
root = tk.Tk()
root.title("Custom Size Messagebox")

# Create a button to trigger the messagebox
button = tk.Button(root, text="Click Me", command=show_custom_size_message)
button.pack(pady=20)

# Run the main loop
root.mainloop()
