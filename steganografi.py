import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb
import os

def pilih_gambar():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
    if file_path:
        entry_gambar.delete(0, tk.END)
        entry_gambar.insert(0, file_path)

def simpan_pesan():
    gambar = entry_gambar.get()
    pesan = entry_pesan.get()
    if not os.path.exists(gambar):
        messagebox.showerror("Error", "Gambar tidak ditemukan.")
        return
    if not pesan:
        messagebox.showwarning("Peringatan", "Masukkan pesan rahasia.")
        return

    hasil_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if hasil_path:
        lsb.hide(gambar, message=pesan).save(hasil_path)
        messagebox.showinfo("Sukses", "Pesan berhasil disisipkan!")

def baca_pesan():
    gambar = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
    if gambar:
        pesan = lsb.reveal(gambar)
        if pesan:
            messagebox.showinfo("Pesan Tersembunyi", pesan)
        else:
            messagebox.showwarning("Kosong", "Tidak ditemukan pesan tersembunyi.")

# GUI
root = tk.Tk()
root.title("Steganografi - Sembunyikan Pesan")

tk.Label(root, text="Pilih Gambar:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_gambar = tk.Entry(root, width=40)
entry_gambar.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=pilih_gambar).grid(row=0, column=2, padx=5)

tk.Label(root, text="Pesan Rahasia:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_pesan = tk.Entry(root, width=40)
entry_pesan.grid(row=1, column=1, padx=5)

tk.Button(root, text="Sisipkan Pesan", command=simpan_pesan, bg='lightblue').grid(row=2, column=1, pady=10)
tk.Button(root, text="Baca Pesan dari Gambar", command=baca_pesan, bg='lightgreen').grid(row=3, column=1, pady=5)

root.mainloop()
