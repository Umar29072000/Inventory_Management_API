import json
from http.server import BaseHTTPRequestHandler
from models import Category, Item

class MyHandler(BaseHTTPRequestHandler):
    def _set_response(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _parse_request_body(self):
        length = int(self.headers.get('Content-Length'))
        return json.loads(self.rfile.read(length))

    def do_GET(self):
        if self.path == "/categories":
            categories = Category.get_all()
            self._set_response()
            self.wfile.write(json.dumps(categories).encode())

        elif self.path.startswith("/items"):
            items = Item.get_all()
            self._set_response()
            self.wfile.write(json.dumps(items).encode())

        else:
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        try:
            data = self._parse_request_body()

            if self.path == "/categories":
                Category.add(data["name"])
                self._set_response(201)
                self.wfile.write(json.dumps({"message": "Category created"}).encode())

            elif self.path == "/items":
                Item.add(data["category_id"], data["name"], data.get("description", ""), data["price"])
                self._set_response(201)
                self.wfile.write(json.dumps({"message": "Item created"}).encode())

        except KeyError as e:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": f"Missing required field: {str(e)}"}).encode())

    def do_PUT(self):
        try:
            item_id = int(self.path.split('/')[-1])
            data = self._parse_request_body()

            with Item.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Item WHERE id = ?", (item_id,))
                if cursor.fetchone() is None:
                    self._set_response(404)
                    self.wfile.write(json.dumps({"error": "Item not found"}).encode())
                    return

                cursor.execute("""
                    UPDATE Item
                    SET name = ?, description = ?, price = ?
                    WHERE id = ?
                """, (data["name"], data.get("description", ""), data["price"], item_id))
                conn.commit()

            self._set_response(200)
            self.wfile.write(json.dumps({"message": "Item updated"}).encode())

        except (ValueError, KeyError) as e:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_DELETE(self):
        try:
            item_id = int(self.path.split('/')[-1])

            with Item.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Item WHERE id = ?", (item_id,))
                if cursor.fetchone() is None:
                    self._set_response(404)
                    self.wfile.write(json.dumps({"error": "Item not found"}).encode())
                    return

                cursor.execute("DELETE FROM Item WHERE id = ?", (item_id,))
                conn.commit()

            self._set_response(200)
            self.wfile.write(json.dumps({"message": "Item deleted"}).encode())

        except ValueError:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": "Invalid item ID"}).encode())
