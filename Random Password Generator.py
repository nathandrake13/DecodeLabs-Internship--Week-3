import tkinter as tk
from tkinter import ttk
import random
import string

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x450")
window.config(bg="#f0f0f0")

style = ttk.Style()
style.configure("TCheckbutton", font=("Helvetica", 12), background="#f0f0f0", foreground="#333333", padding=10)

title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

label_length = tk.Label(window, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
label_length.pack(pady=5)

password_length_slider = tk.Scale(window, from_=8, to=20, orient="horizontal", length=300,
                                   font=("Helvetica", 12), sliderlength=20, showvalue=1,
                                   bg="#f0f0f0", troughcolor="#4CAF50", highlightthickness=0)
password_length_slider.set(12)
password_length_slider.pack(pady=10)

var_symbols = tk.BooleanVar()
var_numbers = tk.BooleanVar()

check_symbols = ttk.Checkbutton(window, text="Include Symbols", variable=var_symbols, style="TCheckbutton")
check_symbols.pack(pady=5)

check_numbers = ttk.Checkbutton(window, text="Include Digits", variable=var_numbers, style="TCheckbutton")
check_numbers.pack(pady=5)

label_password = tk.Label(window, text="Generated Password:", font=("Helvetica", 12), bg="#f0f0f0")
label_password.pack(pady=5)

entry_password = tk.Entry(window, font=("Helvetica", 12), width=30, bd=2, fg="#333333", relief="solid")
entry_password.pack(pady=10)

def generate_password():
    length = password_length_slider.get()
    include_symbols = var_symbols.get()
    include_numbers = var_numbers.get()

    characters = string.ascii_letters
    if include_symbols:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length)) 

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def create_rounded_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, font=("Helvetica", 12, "bold"),
                       bg="#4CAF50", fg="white", relief="flat", height=2, width=20, bd=0)
    button.config(borderwidth=0, highlightthickness=0)
    button.pack(pady=20)
    return button

create_rounded_button(window, "Generate Password", generate_password)

window.mainloop()