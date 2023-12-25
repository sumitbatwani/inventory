from fastapi import APIRouter
from src.db.database import get_items_collection
from src.model.item import ItemIn, ItemOut
from bson import ObjectId

items_router = APIRouter()

@items_router.get("/items")
def get_inventory():
    itemDB = get_items_collection()
    response = itemDB.find({})
    l_items = []
    for doc in response:
        doc["id"] = str(doc["_id"])
        inventoryItem = ItemOut(**doc)
        l_items.append(inventoryItem)

    return {"data": l_items}


@items_router.get("/items/{id}")
def get_inventory(id: str):
    itemDB = get_items_collection()
    # response = itemDB.find_one({"_id": ObjectId(id)})
    response = itemDB.aggregate([{"$match": {"_id": ObjectId(id)}}])
    result = {}
    for r in response:
        r["id"] = str(r["_id"])
        result = ItemOut(**r)

    return {"data": result}


@items_router.post("/item", status_code=200)
def create_inventory(item: ItemIn):
    itemDB = get_items_collection()
    d_item = {**item.dict()}
    id = itemDB.insert_one(d_item).inserted_id
    d_item["id"] = str(id)
    d_item.pop("_id")
    return {"data": d_item}


@items_router.patch("/items/{id}")
def update_inventory(item: ItemIn, id: str):
    itemsDB = get_items_collection()
    itemsDB.update_one({"_id": ObjectId(id)}, {"$set": item.dict()}, upsert=False)
    return {"message": "Success!"}


@items_router.delete("/items/{id}")
def delete_inventory_item(id: str):
    itemDB = get_items_collection()
    itemDB.delete_one({"_id": ObjectId(id)})
    return {"data": "success"}
