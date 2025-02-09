# app/crud.py
from app.models import Item
from app.database import SessionLocal

# For simplicity, we'll use an in-memory store.
# In production, you would use SQLAlchemy sessions to interact with PostgreSQL.

# This is just a placeholder dictionary.
fake_db = {}

def get_item(item_id: int):
    return fake_db.get(item_id)

def create_item(item_data):
    # Create a new item with a simple auto-incremented id.
    new_id = len(fake_db) + 1
    new_item = Item(id=new_id, name=item_data.name, description=item_data.description)
    fake_db[new_id] = new_item
    return new_item
