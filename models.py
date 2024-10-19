import sqlite3

DB_NAME = "inventory.db"

def get_connection():
    """Membuka koneksi ke database SQLite."""
    return sqlite3.connect(DB_NAME)

class Category:
    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Category")
            return cursor.fetchall()

    @staticmethod
    def add(name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Category (name) VALUES (?)", (name,))
            conn.commit()

class Item:
    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Item.*, Category.name as category_name
                FROM Item
                JOIN Category ON Item.category_id = Category.id
            """)
            return cursor.fetchall()

    @staticmethod
    def get_by_id(item_id):
        """Mengambil item berdasarkan ID."""
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Item.*, Category.name as category_name
                FROM Item
                JOIN Category ON Item.category_id = Category.id
                WHERE Item.id = ?
            """, (item_id,))
            return cursor.fetchone()

    @staticmethod
    def add(category_id, name, description, price):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Item (category_id, name, description, price)
                VALUES (?, ?, ?, ?)
            """, (category_id, name, description, price))
            conn.commit()

    @staticmethod
    def update(item_id, name, description, price):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Item
                SET name = ?, description = ?, price = ?
                WHERE id = ?
            """, (name, description, price, item_id))
            conn.commit()

    @staticmethod
    def delete(item_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Item WHERE id = ?", (item_id,))
            conn.commit()
