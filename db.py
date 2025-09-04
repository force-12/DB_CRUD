import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="pdp_crud",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )


#insert data
def create_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO siswa (NIM, Nama, Angkatan, Email) VALUES (%s, %s, %s, %s)", 
                       (NIM, Nama, Angkatan, Email))
    conn.commit()
    conn.close()

def read_siswa():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM siswa ORDER BY Id ASC")
        result = cursor.fetchall()
    conn.close()
    return result

def update_siswa(NIM, Nama, Angkatan, Email):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE siswa SET Nama=%s, Angkatan=%s, Email=%s WHERE NIM=%s", (Nama, Angkatan, Email, NIM))
    conn.commit()
    conn.close()

def delete_siswa(NIM):
    conn = get_connection()
    with conn.cursor() as cursor:
         cursor.execute("DELETE FROM siswa WHERE NIM=%s", (NIM,))
    conn.commit()
    conn.close()
