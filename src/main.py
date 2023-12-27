from db.database import create_indexes
from fastapi import FastAPI
from api.items import items_router

app = FastAPI(title="Inventory Management")

@app.get("/health-check")
def root():
    return {"status": "OK!"}

@app.on_event("startup")
def startup():
    create_indexes()

app.include_router(items_router, prefix="/i/v1", tags=['inventory item'])
