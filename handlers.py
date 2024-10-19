import json
from http.server import BaseHTTPRequestHandler
from models import Category, Item

class MyHandler(BaseHTTPRequestHandler):
    def _set_response(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

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
        length = int(self.headers.get('Content-Length'))
        data = json.loads(self.rfile.read(length))
        
        if self.path == "/categories":
            Category.add(data["name"])
            self._set_response(201)
            self.wfile.write(json.dumps({"message": "Category created"}).encode())
        elif self.path == "/items":
            Item.add(data["category_id"], data["name"], data.get("description", ""), data["price"])
            self._set_response(201)
            self.wfile.write(json.dumps({"message": "Item created"}).encode())
