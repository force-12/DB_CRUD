import streamlit as st
import pandas as pd
import db

st.set_page_config(page_title="Main App", page_icon="📊")

# Cek login
if not st.session_state.get('logged_in', False):
    st.error("Please login first!")
    st.switch_page("login.py")  # kalau belum login, balik ke login

st.title("Halaman Utama Aplikasi")
st.write("Selamat datang di aplikasi!")

if st.button("Logout"):
    st.session_state['logged_in'] = False
    st.switch_page("login.py")

st.title("CRUD SISWA")
menu = st.sidebar.selectbox("Menu", ["Tambah", "Lihat", "Ubah", "Hapus", "Cari Data"])

if menu == "Tambah":
    st.subheader("Tambah Data Siswa")
    NIM = st.text_input("NIM")
    Nama = st.text_input("Nama")
    Angkatan = st.number_input("Angkatan", min_value=2020, max_value=2030, step=1 )
    Email = st.text_input("Email")
    if st.button("Simpan"):
        db.create_siswa(NIM, Nama, Angkatan, Email)
        st.success("Data siswa berhasil ditambahkan!")

elif menu == "Lihat":
    st.subheader("Data Siswa")
    data = db.read_siswa()
    df = pd.DataFrame(data)
    st.dataframe(df)

elif menu == "Ubah":
    st.subheader("Ubah Data Siswa")
    data = db.read_siswa()
    if data:
        nims = [row['NIM'] for row in data]
        selected_nim = st.selectbox("Pilih NIM", nims)
        siswa = next((row for row in data if row['NIM'] == selected_nim), None)
        nim_baru = st.text_input("NIM baru")
        nama_baru = st.text_input("Nama baru")
        angkatan_baru = st.number_input("Angkatan baru", min_value=2020, max_value=2030, step=1)
        email_baru = st.text_input("Email baru")
        if st.button("Ubah"):
            db.update_siswa(selected_nim, nim_baru, nama_baru, angkatan_baru, email_baru)
            st.success("Data siswa berhasil diubah!")
    else:
        st.info("Tidak ada data untuk diubah.")

elif menu == "Hapus":
    st.subheader("Hapus Data Siswa")
    NIM = st.selectbox("Pilih NIM", [row['NIM'] for row in db.read_siswa()])
    if st.button("Hapus"):
        db.delete_siswa(NIM)
        st.success("Data siswa berhasil dihapus!")

elif menu == "Cari Data":
    st.subheader("Cari Data Siswa Berdasarkan NIM")
    nim_cari = st.text_input("Masukkan NIM yang ingin dicari")
    if st.button("Cari"):
        hasil = db.search_siswa(nim_cari)    
        if hasil:
            st.write("Data ditemukan:")
            st.json(hasil)
        else:
            st.warning("Data dengan NIM tersebut tidak ditemukan.")
