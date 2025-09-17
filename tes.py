import psycopg2

def get_connection():
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
