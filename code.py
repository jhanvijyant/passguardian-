import tkinter as tk
from tkinter import ttk, messagebox
import string

# ------------------------ Password Strength Logic ------------------------ #
def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])

    suggestions = []
    if length < 8:
        suggestions.append("Use at least 8 characters")
    if not has_upper:
        suggestions.append("Add uppercase letters")
    if not has_lower:
        suggestions.append("Add lowercase letters")
    if not has_digit:
        suggestions.append("Include numbers")
    if not has_special:
        suggestions.append("Add special characters like @, !, #")

    if length >= 10 and score == 4:
        return "Strong", 100, "green", []
    elif length >= 6 and score >= 2:
        return "Moderate", 60, "orange", suggestions
    else:
        return "Weak", 30, "red", suggestions

# ------------------------ GUI Functions ------------------------ #
def on_key_release(event=None):
    password = entry.get()
    strength, percent, color, tips = check_strength(password)
    strength_label.config(text=f"Strength: {strength}", fg=color)
    progress['value'] = percent
    progress_style.configure("Custom.Horizontal.TProgressbar", background=color)

    suggestion_text.config(state='normal')
    suggestion_text.delete(1.0, tk.END)
    if tips:
        suggestion_text.insert(tk.END, "Suggestions:\n" + "\n".join(f"- {tip}" for tip in tips))
    suggestion_text.config(state='disabled')

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        entry.config(show='')
        toggle_btn.config(text='Hide')

# ------------------------ GUI Setup ------------------------ #
root = tk.Tk()
root.title("🔐 PassGuardian - Password Strength Checker")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#e8f0fe")

progress_style = ttk.Style()
progress_style.theme_use('clam')
progress_style.configure("Custom.Horizontal.TProgressbar", troughcolor='white', thickness=20)

# ------------------------ Widgets ------------------------ #
title = tk.Label(root, text="🔐 PassGuardian", font=("Helvetica", 16, "bold"), bg="#e8f0fe", fg="#2b2d42")
title.pack(pady=10)

subtitle = tk.Label(root, text="Check your password strength in real-time", font=("Helvetica", 10), bg="#e8f0fe")
subtitle.pack()

entry = tk.Entry(root,  width=30, font=("Helvetica", 12))
entry.pack(pady=10)
entry.bind("<KeyRelease>", on_key_release)

frame = tk.Frame(root, bg="#e8f0fe")
frame.pack()

toggle_btn = tk.Button(frame, text="Show", command=toggle_password, font=("Helvetica", 10))
toggle_btn.pack()

progress = ttk.Progressbar(root, style="Custom.Horizontal.TProgressbar", length=300, maximum=100)
progress.pack(pady=15)

strength_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#e8f0fe")
strength_label.pack()

suggestion_text = tk.Text(root, height=6, width=40, font=("Helvetica", 9), wrap="word", bg="#f8f9fa")
suggestion_text.pack(pady=10)
suggestion_text.config(state='disabled')

footer = tk.Label(root, text="Created by Jhanvi ❤️", font=("Arial", 9), bg="#e8f0fe", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
