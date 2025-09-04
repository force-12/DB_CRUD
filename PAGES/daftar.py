import streamlit as st
from db import get_connection

st.set_page_config(page_title="Register Page", page_icon="📝")

st.title("Register Page")

new_user = st.text_input("Buat Username")
new_pass = st.text_input("Buat Password", type="password")

if st.button("Daftar"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE username=%s", (new_user,))
    if cursor.fetchone():
        st.error("Username sudah terdaftar.")
    elif new_user == "" or new_pass == "":
        st.error("Username/Password tidak boleh kosong.")
    else:
        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (new_user, new_pass))
        conn.commit()
        st.success("Registrasi berhasil! Silakan login.")
        st.switch_page("login.py")  # balik ke login

    conn.close()

if st.button("Kembali ke Login"):
    st.switch_page("login.py")
