# New file gui.py
import tkinter as tk
from tkinter import messagebox
from main import check_password_strength

def evaluate_password():
    password = entry.get()
    result = check_password_strength(password)

    message = f"Password Strength: {result['strength']} ({result['score']}/5)\n"
    if result["feedback"]:
        message += "\nFeedback:\n" + "\n".join(f"- {msg}" for msg in result["feedback"])

    messagebox.showinfo("Password Strength", message)

# Create GUI window
root = tk.Tk()
root.title("Password Strength Checker")

# Input field
tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

# Check Button
tk.Button(root, text="Check Strength", command=evaluate_password).pack(pady=10)

# Run the application
root.mainloop()