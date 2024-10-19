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
- Docker dan Docker Compose – Untuk containerisasi.
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

## Jalankan menggunakan Docker

### Build Image Docker:

```bash
docker-compose build
```

### Jalankan Container:

```bash
docker-compose up
```

Jika berhasil, Anda akan melihat pesan:

```bash
Server running on port 8000...
```

## Penggunaan API

### 1. GET /categories

Endpoint:

```bash
GET http://localhost:8000/categories
```

Response:

```bash
[
  { "id": 1, "name": "Electronics" }
]
```

### 2. POST /categories

Endpoint:

```bash
POST http://localhost:8000/categories
```

Body:

```bash
{
  "name": "Electronics"
}
```

Response:

```bash
{ 
    "message": "Category created"
}
```

### 3. GET /items

Endpoint:

```bash
GET http://localhost:8000/items
```

Response:

```bash
[
  {
    "id": 1,
    "category_id": 1,
    "name": "Laptop",
    "description": "Gaming Laptop",
    "price": 1500.0,
    "created_at": "2024-10-19 12:00:00",
    "category_name": "Electronics"
  }
]
```

### 4. GET /items/{id}

Endpoint:

```bash
GET http://localhost:8000/items/1
```

Response:

```bash
{
  "id": 1,
  "category_id": 1,
  "name": "Laptop",
  "description": "Gaming Laptop",
  "price": 1500.0,
  "created_at": "2024-10-19 12:00:00",
  "category_name": "Electronics"
}
```

### 5. POST /items

Endpoint:

```bash
POST http://localhost:8000/items
```

Body:

```bash
{
  "category_id": 1,
  "name": "Laptop",
  "description": "Gaming Laptop",
  "price": 1500.0
}
```

Response:

```bash
{
    "message": "Item created"
}
```

### 6. PUT /items/{id}

Endpoint:

```bash
PUT http://localhost:8000/items/1
```

Body:

```bash
{
  "name": "Laptop Pro",
  "description": "High-end Gaming Laptop",
  "price": 1800.0
}
```

Response:

```bash
{
    "message": "Item updated"
}
```

### 4. GET /items/{id}

Endpoint:

```bash
DELETE http://localhost:8000/items/1
```

Response:

```bash
{
    "message": "Item deleted"
}
```