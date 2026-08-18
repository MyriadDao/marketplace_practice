from pydantic import BaseModel, Field, ConfigDict
class ProductResponse(BaseModel):
    name: str
    price: float
    category: int
    description: str
    in_stock: float

    model_config = ConfigDict(from_attributes=True)