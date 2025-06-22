import tkinter as tk
from tkinter import ttk

# Fungsi Caesar Cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Fungsi tombol
def process_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_var.get()
    if mode.get() == 'Enkripsi':
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# GUI Setup
window = tk.Tk()
window.title("Caesar Cipher GUI")
window.geometry("400x400")

# Judul
ttk.Label(window, text="Caesar Cipher", font=("Helvetica", 16)).pack(pady=10)

# Input teks
ttk.Label(window, text="Masukkan Teks:").pack()
input_text = tk.Text(window, height=4, width=40)
input_text.pack()

# Pilihan shift
ttk.Label(window, text="Jumlah Huruf Digeser:").pack(pady=5)
shift_var = tk.IntVar(value=3)
shift_spin = ttk.Spinbox(window, from_=1, to=25, textvariable=shift_var, width=5)
shift_spin.pack()

# Pilihan mode
mode = tk.StringVar(value='Enkripsi')
ttk.Radiobutton(window, text='Enkripsi', variable=mode, value='Enkripsi').pack()
ttk.Radiobutton(window, text='Dekripsi', variable=mode, value='Dekripsi').pack()

# Tombol proses
ttk.Button(window, text="Proses", command=process_text).pack(pady=10)

# Output teks
ttk.Label(window, text="Hasil:").pack()
output_text = tk.Text(window, height=4, width=40)
output_text.pack()

# Jalankan aplikasi
window.mainloop()
