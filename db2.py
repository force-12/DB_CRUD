import psycopg2

def get_connection():
    """Koneksi ke Supabase PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host="gyohfzvugbusjcbsmffu.supabase.co",
            port=5432,
            database="postgres",
            user="postgres",
            password="@Mrcyber12345"
        )
        return conn
    except Exception as e:
        print(f"Gagal koneksi: {e}")
        return None

# ===== CRUD Siswa =====
def create_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO siswa (NIM, Nama, Angkatan, Email) VALUES (%s, %s, %s, %s)",
                (NIM, Nama, Angkatan, Email)
            )
            conn.commit()
        conn.close()

def read_siswa():
    conn = get_connection()
    result = []
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM siswa ORDER BY id ASC")
            result = cur.fetchall()
        conn.close()
    return result

def update_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE siswa SET Nama=%s, Angkatan=%s, Email=%s WHERE NIM=%s",
                (Nama, Angkatan, Email, NIM)
            )
            conn.commit()
        conn.close()

def delete_siswa(NIM):
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM siswa WHERE NIM=%s", (NIM,))
            conn.commit()
        conn.close()

def search_siswa(NIM):
    conn = get_connection()
    result = []
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM siswa WHERE NIM=%s", (NIM,))
            result = cur.fetchall()
        conn.close()
    return result

# ===== CRUD User (login) =====
def check_user(username, password):
    """Cek username & password di tabel user"""
    conn = get_connection()
    result = False
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM users WHERE username=%s AND password=%s",
                (username, password)
            )
            if cur.fetchone():
                result = True
        conn.close()
    return result
