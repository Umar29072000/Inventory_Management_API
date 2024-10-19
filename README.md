# Inventory_Management_API

## Fitur Utama API

### Kategori:
- GET /categories: Mendapatkan daftar kategori.
- POST /categories: Menambahkan kategori baru.

### Item:
- GET /items: Mendapatkan daftar item beserta informasi kategorinya.
- GET /items/{id}: Mendapatkan detail item berdasarkan ID.
- POST /items: Menambahkan item baru.
- PUT /items/{id}: Memperbarui item berdasarkan ID.
- GET /categories: Mendapatkan daftar kategori.
- DELETE /items/{id}: Menghapus item berdasarkan ID.

## Teknologi yang digunakan

- Python 3.12.7 – Backend API.
- SQLite – Database lokal.
- http.server – Library Python untuk server HTTP.
- Postman – Untuk testing API.

## Langkah setup dan instalasi

### Langkah 1: Clone Repository

```bash
git clone https://github.com/Umar29072000/Inventory_Management_API.git
cd project
```

### Langkah 2: Setup Database

```bash
sqlite3 inventory.db < database_setup.sql
```

### Langkah 3: Jalankan Server

```bash
python main.py
```

Jika berhasil, Anda akan melihat pesan:

```bash
Server running on port 8000...
```
