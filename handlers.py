import re
import json
from http.server import BaseHTTPRequestHandler
from models import Category, Item

class MyHandler(BaseHTTPRequestHandler):
    def _set_response(self, status=200, content_type="application/json"):
        """Mengatur response header termasuk CORS."""
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def _parse_request_body(self):
        """Parse body JSON dari request."""
        length = int(self.headers.get('Content-Length'))
        return json.loads(self.rfile.read(length))

    def do_OPTIONS(self):
        """Menangani preflight request untuk CORS."""
        self._set_response(204)

    def do_GET(self):
        if self.path == "/categories":
            categories = Category.get_all()
            self._set_response()
            self.wfile.write(json.dumps(categories).encode())

        elif re.match(r"^/items/\d+$", self.path):
            item_id = int(self.path.split('/')[-1])
            item = Item.get_by_id(item_id)
            if item:
                self._set_response()
                self.wfile.write(json.dumps(item).encode())
            else:
                self._set_response(404)
                self.wfile.write(json.dumps({"error": "Item not found"}).encode())

        elif self.path == "/items":
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
            Item.update(item_id, data["name"], data.get("description", ""), data["price"])
            self._set_response(200)
            self.wfile.write(json.dumps({"message": "Item updated"}).encode())

        except (ValueError, KeyError) as e:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_DELETE(self):
        try:
            item_id = int(self.path.split('/')[-1])
            Item.delete(item_id)
            self._set_response(200)
            self.wfile.write(json.dumps({"message": "Item deleted"}).encode())

        except ValueError:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": "Invalid item ID"}).encode())
