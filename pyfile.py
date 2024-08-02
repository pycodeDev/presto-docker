from pyhive import presto
import pandas as pd

# Menghubungkan ke server Presto
conn = presto.connect(
    host='host.docker.internal',  # Ganti dengan alamat server Presto Anda
    port=8080,         # Port yang dipetakan dari kontainer Docker Presto
    catalog='mysql',   # Nama katalog sesuai yang didefinisikan di mysql.properties
    schema='c45_project',  # Nama database atau skema MySQL
    username='anang',  # Username Anda
    password='12345678'   # Password Anda
)

# Menjalankan query SQL
query = "SELECT * FROM tb_data LIMIT 10"
df = pd.read_sql(query, conn)

# Menampilkan hasilnya
print(df)

# Menutup koneksi
conn.close()
