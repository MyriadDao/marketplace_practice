from pydantic import BaseModel, Field, ConfigDict
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str
    in_stock: float

    model_config = ConfigDict(from_attributes=True)