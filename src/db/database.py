from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.inventory

def get_items_collection():
    return db.items