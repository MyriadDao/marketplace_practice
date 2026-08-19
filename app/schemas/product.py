from pydantic import BaseModel, Field, ConfigDict
class ProductResponse(BaseModel):
    title: str
    price: float
    category: str
    description: str

    model_config = ConfigDict(from_attributes=True)