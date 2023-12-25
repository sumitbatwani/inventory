from pydantic import BaseModel

class ItemIn(BaseModel):
    name: str
    quantity: int


class ItemOut(ItemIn):
    id: str
