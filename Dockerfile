# Gunakan image resmi Trino (Presto)
FROM trinodb/trino:latest

# Tambahkan konfigurasi MySQL
COPY conf/mysql.properties /usr/lib/presto/etc/catalog/mysql.properties

# Tambahkan konfigurasi server Presto
COPY conf/config.properties /usr/lib/presto/etc/config.properties
COPY conf/access-control.properties /usr/lib/presto/etc/access-control.properties
