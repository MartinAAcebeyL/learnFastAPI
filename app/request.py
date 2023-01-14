from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str
    age: int
    address: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(
        gt=0, description="The price must be greater than zero")
    tax: float | None = None
