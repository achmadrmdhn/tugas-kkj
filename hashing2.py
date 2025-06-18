import tkinter as tk
from tkinter import messagebox, scrolledtext
import hashlib
import pyperclip # Pastikan Anda sudah menginstal ini: pip install pyperclip

def generate_hash():
    """Generates the hash of the input text based on selected algorithm."""
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to hash.")
        return

    selected_algorithm = hash_algorithm.get()
    encoded_input = input_text.encode('utf-8')
    hashed_result = ""

    if selected_algorithm == "MD5":
        hashed_result = hashlib.md5(encoded_input).hexdigest()
    elif selected_algorithm == "SHA-256":
        hashed_result = hashlib.sha256(encoded_input).hexdigest()
    elif selected_algorithm == "SHA-512":
        hashed_result = hashlib.sha512(encoded_input).hexdigest()
    else:
        messagebox.showerror("Error", "Invalid hashing algorithm selected.")
        return

    hash_output.config(state=tk.NORMAL)  # Enable editing
    hash_output.delete("1.0", tk.END)
    hash_output.insert(tk.END, hashed_result)
    hash_output.config(state=tk.DISABLED)  # Disable editing

def copy_to_clipboard():
    """Copies the generated hash to the clipboard."""
    hash_value = hash_output.get("1.0", tk.END).strip()
    if hash_value:
        try:
            pyperclip.copy(hash_value)
            messagebox.showinfo("Copied!", "Hash copied to clipboard.")
        except Exception as e:
            messagebox.showerror("Copy Error", f"Failed to copy to clipboard: {e}")
    else:
        messagebox.showwarning("Empty", "No hash to copy.")

def clear_fields():
    """Clears all input and output fields."""
    text_input.delete("1.0", tk.END)
    hash_output.config(state=tk.NORMAL)
    hash_output.delete("1.0", tk.END)
    hash_output.config(state=tk.DISABLED)

# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced Hashing Tool")
root.geometry("600x450")
root.resizable(False, False)
root.configure(bg="#2c3e50") # Dark background

# Style Configuration
FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 10)
FONT_BUTTON = ("Arial", 10, "bold")
COLOR_BG_PRIMARY = "#34495e" # Darker background for frames
COLOR_TEXT_PRIMARY = "#ecf0f1" # Light text color
COLOR_BUTTON_GENERATE = "#27ae60" # Green
COLOR_BUTTON_COPY = "#3498db" # Blue
COLOR_BUTTON_CLEAR = "#e74c3c" # Red
COLOR_BORDER = "#1abc9c" # Teal border

# Input Section
input_frame = tk.LabelFrame(root, text="Enter Text", font=FONT_LABEL, fg=COLOR_TEXT_PRIMARY,
                           bg=COLOR_BG_PRIMARY, padx=15, pady=15, bd=2, relief="groove")
input_frame.pack(pady=15, padx=20, fill="x")

text_input = scrolledtext.ScrolledText(input_frame, height=6, width=60, wrap="word",
                                        bd=2, relief="flat", bg="#ecf0f1", fg="#2c3e50",
                                        insertbackground="#2c3e50", font=("Consolas", 10))
text_input.pack(pady=8)

# Algorithm Selection
algorithm_frame = tk.Frame(root, bg="#2c3e50")
algorithm_frame.pack(pady=5, padx=20, fill="x")

tk.Label(algorithm_frame, text="Select Algorithm:", font=FONT_LABEL, fg=COLOR_TEXT_PRIMARY, bg="#2c3e50").pack(side=tk.LEFT, padx=(0, 10))

hash_algorithm = tk.StringVar(root)
hash_algorithm.set("MD5") # default value
algorithms = ["MD5", "SHA-256", "SHA-512"]
algorithm_menu = tk.OptionMenu(algorithm_frame, hash_algorithm, *algorithms)
algorithm_menu.config(bg=COLOR_BG_PRIMARY, fg=COLOR_TEXT_PRIMARY, font=FONT_LABEL, bd=0, highlightbackground=COLOR_BG_PRIMARY, activebackground="#4a6078")
algorithm_menu["menu"].config(bg=COLOR_BG_PRIMARY, fg=COLOR_TEXT_PRIMARY, font=FONT_LABEL)
algorithm_menu.pack(side=tk.LEFT)

# Buttons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=10, padx=20)

generate_button = tk.Button(button_frame, text="Generate Hash", command=generate_hash,
                           font=FONT_BUTTON, bg=COLOR_BUTTON_GENERATE, fg="white",
                           activebackground="#229954", activeforeground="white",
                           bd=0, padx=15, pady=8)
generate_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copy Hash", command=copy_to_clipboard,
                       font=FONT_BUTTON, bg=COLOR_BUTTON_COPY, fg="white",
                       activebackground="#2980b9", activeforeground="white",
                       bd=0, padx=15, pady=8)
copy_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_fields,
                        font=FONT_BUTTON, bg=COLOR_BUTTON_CLEAR, fg="white",
                        activebackground="#c0392b", activeforeground="white",
                        bd=0, padx=15, pady=8)
clear_button.pack(side=tk.LEFT, padx=10)

# Output Section
output_frame = tk.LabelFrame(root, text="Hashed Output", font=FONT_LABEL, fg=COLOR_TEXT_PRIMARY,
                            bg=COLOR_BG_PRIMARY, padx=15, pady=15, bd=2, relief="groove")
output_frame.pack(pady=15, padx=20, fill="x")

hash_output = scrolledtext.ScrolledText(output_frame, height=3, width=60, wrap="word",
                                       bd=2, relief="flat", bg="#ecf0f1", fg="#2c3e50",
                                       insertbackground="#2c3e50", font=("Courier New", 10), state=tk.DISABLED)
hash_output.pack(pady=8)

# Run the application
root.mainloop()