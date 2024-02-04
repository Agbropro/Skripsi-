import tkinter as tk
from tkinter import messagebox

def show_about():
    messagebox.showinfo("About", "This is a Simple GUI with Menus")

def show_help():
    messagebox.showinfo("Help", "You can customize this GUI as needed.")

def open_file():
    messagebox.showinfo("Open", "Opening a file...")

def save_file():
    messagebox.showinfo("Save", "Saving the file...")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("GUI with Menus")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Help", command=show_help)

# Run the main loop
root.mainloop()