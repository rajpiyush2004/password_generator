import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Password Generator")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(column=0, row=0, sticky=tk.W)

length_entry = ttk.Entry(frame)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

generate_button = ttk.Button(frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(column=0, row=1, columnspan=2, pady=10)

password_label = ttk.Label(frame, text="Generated Password:")
password_label.grid(column=0, row=2, sticky=tk.W)

password_entry = ttk.Entry(frame, state="readonly")
password_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))
password_entry.config(font=("Arial", 12), foreground="blue")

# Set the size of the GUI window
root.geometry("400x300")


# Start the GUI event loop
root.mainloop()
