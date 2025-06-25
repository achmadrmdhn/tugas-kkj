import streamlit as st
from PIL import Image
from stegano import lsb
import os
import hashlib
# import pyperclip # Note: pyperclip is not directly usable in a web environment like Streamlit for client-side clipboard access. We'll simulate it or inform the user to copy manually.
# import tkinter as tk # Not directly usable in Streamlit as it's a web framework. We will adapt the logic.
# from tkinter import filedialog, messagebox # Not directly usable in Streamlit. We will adapt the logic.


# --- Steganography Functions (Adapted for Streamlit) ---
def steganography_section():
    st.header("Steganografi")

    st.write("Steganografi adalah seni dan ilmu menyembunyikan pesan rahasia di dalam media lain (seperti gambar, audio, video, atau teks) sehingga keberadaan pesan tersebut tidak diketahui atau tidak disadari oleh pihak selain pengirim dan penerima yang dituju.")

    # Hide Message
    st.subheader("Sisipkan Pesan")
    uploaded_image_hide = st.file_uploader("Pilih Gambar untuk Menyisipkan Pesan", type=["jpg", "jpeg", "png"], key="hide_image")
    message_to_hide = st.text_area("Masukkan Pesan Rahasia", key="message_hide")

    if st.button("Sisipkan Pesan", key="do_hide"):
        if uploaded_image_hide and message_to_hide:
            try:
                # Save the uploaded image temporarily
                with open("temp_image_hide.png", "wb") as f:
                    f.write(uploaded_image_hide.read())

                img = Image.open("temp_image_hide.png")
                
                # Ensure image is in a compatible mode (e.g., RGB)
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGB')
                img.save("temp_image_hide.png") # Resave in compatible mode if converted

                # Perform steganography
                hidden_image = lsb.hide("temp_image_hide.png", message=message_to_hide)
                
                # Provide download
                st.success("Pesan berhasil disisipkan! Unduh gambar yang sudah disisipkan:")
                img_byte_arr = io.BytesIO()
                hidden_image.save(img_byte_arr, format="PNG")
                st.download_button(
                    label="Unduh Gambar dengan Pesan Tersembunyi",
                    data=img_byte_arr.getvalue(),
                    file_name="gambar_tersembunyi.png",
                    mime="image/png"
                )
                os.remove("temp_image_hide.png") # Clean up
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menyisipkan pesan: {e}")
        else:
            st.warning("Mohon unggah gambar dan masukkan pesan.")

    st.markdown("---")

    # Reveal Message
    st.subheader("Baca Pesan dari Gambar")
    uploaded_image_reveal = st.file_uploader("Pilih Gambar untuk Membaca Pesan", type=["jpg", "jpeg", "png"], key="reveal_image")

    if st.button("Baca Pesan", key="do_reveal"):
        if uploaded_image_reveal:
            try:
                # Save the uploaded image temporarily
                with open("temp_image_reveal.png", "wb") as f:
                    f.write(uploaded_image_reveal.read())

                # Perform reveal
                revealed_message = lsb.reveal("temp_image_reveal.png")
                if revealed_message:
                    st.info(f"Pesan Tersembunyi: `{revealed_message}`")
                else:
                    st.warning("Tidak ditemukan pesan tersembunyi dalam gambar ini.")
                os.remove("temp_image_reveal.png") # Clean up
            except Exception as e:
                st.error(f"Terjadi kesalahan saat membaca pesan: {e}")
        else:
            st.warning("Mohon unggah gambar untuk membaca pesan.")

# --- Hashing Functions (Adapted for Streamlit) ---
def hashing_section():
    st.header("Hashing")

    st.write("Hashing adalah proses mengubah data input (yang bisa berupa teks, file, atau data apa pun dengan ukuran bervariasi) menjadi sebuah string alfanumerik dengan panjang tetap, yang disebut hash atau nilai hash. Proses ini dilakukan menggunakan fungsi hash atau algoritma hash.")

    # Inisialisasi session_state untuk input dan output hashing jika belum ada
    if 'hash_input_text_state' not in st.session_state:
        st.session_state.hash_input_text_state = ""
    if 'hash_output_area_state' not in st.session_state:
        st.session_state.hash_output_area_state = ""

    # Gunakan value dan on_change untuk mengikat widget ke session_state
    input_text = st.text_area(
        "Masukkan Teks untuk di-Hash",
        height=150,
        key="hash_input_text",
        value=st.session_state.hash_input_text_state,
        on_change=lambda: setattr(st.session_state, 'hash_input_text_state', st.session_state.hash_input_text)
    )

    hash_algorithm = st.selectbox("Pilih Algoritma Hashing", ["MD5", "SHA-256", "SHA-512"], key="hash_algo_select")

    hashed_result = ""
    if st.button("Generate Hash", key="generate_hash_button"):
        if input_text:
            encoded_input = input_text.encode('utf-8')
            if hash_algorithm == "MD5":
                hashed_result = hashlib.md5(encoded_input).hexdigest()
            elif hash_algorithm == "SHA-256":
                hashed_result = hashlib.sha256(encoded_input).hexdigest()
            elif hash_algorithm == "SHA-512":
                hashed_result = hashlib.sha512(encoded_input).hexdigest()
            
            # Perbarui state output
            st.session_state.hash_output_area_state = hashed_result
            st.text_area("Hasil Hash", value=st.session_state.hash_output_area_state, height=100, disabled=True, key="hash_output_area")
            
            if hashed_result:
                st.code(hashed_result, language='text')
                st.success("Hash berhasil dibuat!")
                st.info("Anda bisa menyalin hash di atas secara manual.")
        else:
            st.warning("Mohon masukkan teks untuk di-hash.")
    else: # Ini penting agar output_area menampilkan nilai dari session_state setelah rerun
         st.text_area("Hasil Hash", value=st.session_state.hash_output_area_state, height=100, disabled=True, key="hash_output_area")


    # Fungsi untuk membersihkan field
    def clear_hashing_fields():
        st.session_state.hash_input_text_state = ""
        st.session_state.hash_output_area_state = ""
        # Tidak perlu st.experimental_rerun() jika state diatur langsung

    if st.button("Bersihkan", key="clear_hash_fields", on_click=clear_hashing_fields):
        # Tombol akan memanggil clear_hashing_fields() saat diklik,
        # dan Streamlit akan me-rerun secara otomatis setelah on_click
        pass # Tidak perlu kode di sini karena on_click sudah menangani

# --- Caesar Cipher Functions (Adapted for Streamlit) ---
def caesar_cipher_section():
    st.header("Kriptografi")

    st.write("Kriptografi metode Caesar Cipher adalah salah satu metode enkripsi tertua dan paling sederhana dalam kriptografi. Dinamakan demikian karena konon digunakan oleh Julius Caesar untuk mengamankan komunikasi militernya.")

    input_text = st.text_area("Masukkan Teks", height=150, key="caesar_input_text")

    shift_amount = st.slider("Jumlah Geseran (Shift)", min_value=1, max_value=25, value=3, key="caesar_shift_slider")

    mode = st.radio("Pilih Mode", ('Enkripsi', 'Dekripsi'), key="caesar_mode_radio")

    result_text = ""
    if st.button("Proses", key="process_caesar_button"):
        text = input_text.strip()
        if text:
            if mode == 'Enkripsi':
                result_text = caesar_encrypt(text, shift_amount)
            else:
                result_text = caesar_decrypt(text, shift_amount)
            st.text_area("Hasil", value=result_text, height=100, disabled=True, key="caesar_output_area")
            st.success("Proses selesai!")
        else:
            st.warning("Mohon masukkan teks untuk diproses.")

# Fungsi Caesar Cipher (tetap sama)
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

# --- Main Streamlit App ---
import io # Needed for handling image bytes

st.set_page_config(
    page_title="Dashboard Keamanan Sederhana",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigasi")
app_mode = st.sidebar.radio(
    "Pilih Fitur:",
    ["Steganografi", "Hashing", "Kriptografi"]
)

st.title("Dashboard Keamanan Sederhana")
st.write("Selamat datang di Dashboard Keamanan Sederhana. Pilih fitur dari sidebar untuk memulai.")

if app_mode == "Steganografi":
    steganography_section()
elif app_mode == "Hashing":
    hashing_section()
elif app_mode == "Kriptografi":
    caesar_cipher_section()