import tkinter as tk
from tkinter import messagebox
import hashlib

def generate_hash():
    """
    Fungsi untuk menghasilkan hash dari input teks.
    """
    input_text = entry_input.get()
    if not input_text:
        messagebox.showwarning("Peringatan", "Masukkan teks yang ingin di-hash.")
        return

    # Hashing menggunakan SHA-256
    try:
        input_bytes = input_text.encode('utf-8')
        sha256_hash_obj = hashlib.sha256()
        sha256_hash_obj.update(input_bytes)
        sha256_digest = sha256_hash_obj.hexdigest()

        # Tampilkan hasil
        text_output.delete("1.0", tk.END) # Hapus teks sebelumnya
        text_output.insert(tk.END, f"Teks Asli:\n{input_text}\n\n")
        text_output.insert(tk.END, f"Hash SHA-256:\n{sha256_digest}\n\n")
        text_output.insert(tk.END, "Panjang Hash (karakter): 64\n")
        text_output.insert(tk.END, "Panjang Hash (bit): 256\n")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

def compare_hashes():
    """
    Fungsi untuk membandingkan dua teks dan hash-nya.
    """
    text1 = entry_compare1.get()
    text2 = entry_compare2.get()

    if not text1 or not text2:
        messagebox.showwarning("Peringatan", "Masukkan kedua teks untuk perbandingan.")
        return

    hash1 = hashlib.sha256(text1.encode('utf-8')).hexdigest()
    hash2 = hashlib.sha256(text2.encode('utf-8')).hexdigest()

    text_comparison_output.delete("1.0", tk.END)
    text_comparison_output.insert(tk.END, f"Teks 1: '{text1}'\nHash 1: {hash1}\n\n")
    text_comparison_output.insert(tk.END, f"Teks 2: '{text2}'\nHash 2: {hash2}\n\n")

    if hash1 == hash2:
        text_comparison_output.insert(tk.END, "Status: HASH KEDUA TEKS SAMA (Kemungkinan teksnya sama persis)\n", "green_text")
    else:
        text_comparison_output.insert(tk.END, "Status: HASH KEDUA TEKS BERBEDA (Teksnya tidak sama persis)\n", "red_text")

# --- GUI Setup ---
root = tk.Tk()
root.title("Aplikasi Hashing (SHA-256)")
root.geometry("700x650") # Atur ukuran jendela

# Frame untuk Generate Hash
frame_generate = tk.LabelFrame(root, text="Generate Hash SHA-256", padx=15, pady=15)
frame_generate.pack(padx=20, pady=10, fill="x")

tk.Label(frame_generate, text="Masukkan Teks:").grid(row=0, column=0, sticky="w", pady=5)
entry_input = tk.Entry(frame_generate, width=70)
entry_input.grid(row=0, column=1, padx=5, pady=5)

btn_generate = tk.Button(frame_generate, text="Generate Hash", command=generate_hash, bg='lightblue', fg='black')
btn_generate.grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame_generate, text="Hasil Hash:").grid(row=1, column=0, sticky="nw", pady=5)
text_output = tk.Text(frame_generate, width=80, height=8, wrap="word", relief="groove", borderwidth=2)
text_output.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Frame untuk Compare Hashes
frame_compare = tk.LabelFrame(root, text="Bandingkan Dua Teks", padx=15, pady=15)
frame_compare.pack(padx=20, pady=10, fill="x")

tk.Label(frame_compare, text="Teks 1:").grid(row=0, column=0, sticky="w", pady=5)
entry_compare1 = tk.Entry(frame_compare, width=70)
entry_compare1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_compare, text="Teks 2:").grid(row=1, column=0, sticky="w", pady=5)
entry_compare2 = tk.Entry(frame_compare, width=70)
entry_compare2.grid(row=1, column=1, padx=5, pady=5)

btn_compare = tk.Button(frame_compare, text="Bandingkan Hash", command=compare_hashes, bg='lightgreen', fg='black')
btn_compare.grid(row=1, column=2, padx=5, pady=5)

tk.Label(frame_compare, text="Hasil Perbandingan:").grid(row=2, column=0, sticky="nw", pady=5)
text_comparison_output = tk.Text(frame_compare, width=80, height=8, wrap="word", relief="groove", borderwidth=2)
text_comparison_output.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Konfigurasi tag warna untuk output perbandingan
text_comparison_output.tag_config("green_text", foreground="green", font=("Helvetica", 10, "bold"))
text_comparison_output.tag_config("red_text", foreground="red", font=("Helvetica", 10, "bold"))

root.mainloop()