from fastapi import FastAPI
from src.api.items import items_router

app = FastAPI(title="Inventory Management")

@app.get("/health-check")
def root():
    return {"status": "OK!"}

app.include_router(items_router, prefix="/i/v1", tags=['inventory item'])
