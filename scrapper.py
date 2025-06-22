import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url, tag_name, class_name=None):
    """
    Fungsi untuk melakukan scraping pada URL yang diberikan.
    Mengambil elemen berdasarkan tag HTML dan opsional class name.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memunculkan HTTPError untuk status kode yang buruk (4xx atau 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        if class_name:
            elements = soup.find_all(tag_name, class_=class_name)
        else:
            elements = soup.find_all(tag_name)

        data = [element.get_text(strip=True) for element in elements]
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Terjadi kesalahan saat mengakses URL: {e}")
        return []
    except Exception as e:
        st.error(f"Terjadi kesalahan lain: {e}")
        return []

def main():
    st.title("Web Scraping Tool")
    st.write("Alat sederhana untuk mengekstraksi data dari situs web.")

    st.sidebar.header("Pengaturan Scraping")
    url_input = st.sidebar.text_input("Masukkan URL situs web:", "https://www.example.com")
    tag_input = st.sidebar.text_input("Masukkan nama tag HTML (misal: p, h1, a, div):", "p")
    class_input = st.sidebar.text_input("Masukkan nama kelas CSS (opsional):", "")

    if st.sidebar.button("Mulai Scraping"):
        if not url_input or not tag_input:
            st.error("URL dan nama tag tidak boleh kosong.")
            return

        with st.spinner("Sedang melakukan scraping..."):
            scraped_data = scrape_website(url_input, tag_input, class_input if class_input else None)

            if scraped_data:
                st.success(f"Ditemukan {len(scraped_data)} elemen.")
                df = pd.DataFrame(scraped_data, columns=[f"Data dari <{tag_input}>"])
                st.dataframe(df)

                st.download_button(
                    label="Download Data sebagai CSV",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name=f"scraped_data_{tag_input}.csv",
                    mime="text/csv",
                )
            else:
                st.info("Tidak ada data yang ditemukan atau terjadi kesalahan.")

if __name__ == "__main__":
    main()