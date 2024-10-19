import unittest
from models import Category, Item

class TestAPI(unittest.TestCase):
    def test_add_category(self):
        Category.add("Test Category")
        categories = Category.get_all()
        self.assertTrue(any(c[1] == "Test Category" for c in categories))

    def test_add_item(self):
        Item.add(1, "Test Item", "Description", 10.0)
        items = Item.get_all()
        self.assertTrue(any(i[2] == "Test Item" for i in items))

if __name__ == "__main__":
    unittest.main()
