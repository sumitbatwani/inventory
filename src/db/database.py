from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.inventory

def create_indexes():
    db.items.create_index({"customerId": 1})

def get_items_collection():
    return db.items