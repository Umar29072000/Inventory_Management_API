-- Membuat tabel Category
CREATE TABLE IF NOT EXISTS Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Membuat tabel Item dengan relasi ke Category
CREATE TABLE IF NOT EXISTS Item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Category (id)
);

-- Membuat index untuk optimasi
CREATE INDEX idx_category_name ON Category (name);
CREATE INDEX idx_item_name ON Item (name);
CREATE INDEX idx_item_category ON Item (category_id);
