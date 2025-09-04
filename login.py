import streamlit as st
from db import get_connection

st.set_page_config(page_title="Login Page", page_icon="🔐")

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()

    if result:
        st.session_state['logged_in'] = True
        st.success("Login berhasil!")
        st.switch_page("pages/app.py")
    else:
        st.error("Username / Password salah.")

    conn.close()

if st.button("Daftar jika belum ada akun"):
    st.switch_page("pages/daftar.py")
