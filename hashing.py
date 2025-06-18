import tkinter as tk
from tkinter import messagebox
import hashlib

def generate_md5_hash():
    """Generates the MD5 hash of the input text and displays it."""
    input_text = text_input.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text to hash.")
        return

    md5_hash = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    hash_output.config(state=tk.NORMAL)  # Enable editing
    hash_output.delete("1.0", tk.END)
    hash_output.insert(tk.END, md5_hash)
    hash_output.config(state=tk.DISABLED)  # Disable editing

# --- GUI Setup ---
root = tk.Tk()
root.title("MD5 Hashing Tool")
root.geometry("500x350")
root.resizable(False, False) # Disable window resizing

# Input Section
input_frame = tk.LabelFrame(root, text="Enter Text", padx=10, pady=10)
input_frame.pack(pady=10, padx=10, fill="x")

text_input = tk.Text(input_frame, height=5, width=50, wrap="word", bd=2, relief="groove")
text_input.pack(pady=5)

# Button
hash_button = tk.Button(root, text="Generate MD5 Hash", command=generate_md5_hash, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white")
hash_button.pack(pady=10)

# Output Section
output_frame = tk.LabelFrame(root, text="MD5 Hash Output", padx=10, pady=10)
output_frame.pack(pady=10, padx=10, fill="x")

hash_output = tk.Text(output_frame, height=2, width=50, wrap="word", bd=2, relief="groove", state=tk.DISABLED, font=("Courier New", 10))
hash_output.pack(pady=5)

# Run the application
root.mainloop()