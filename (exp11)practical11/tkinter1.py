#Rollno-12
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tkinter GUI Application")
root.geometry("400x300")

# Function for button click
def display():
    name = entry.get()
    messagebox.showinfo("Welcome", "Hello, " + name)

# Create label
label = tk.Label(root, text="Welcome to Tkinter GUI",
                 font=("Arial", 16))
label.pack(pady=20)

# Create input label
tk.Label(root, text="Enter Your Name:").pack()

# Create text box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create button
button = tk.Button(root, text="Submit",
                   command=display)
button.pack(pady=10)

# Run application
root.mainloop()
