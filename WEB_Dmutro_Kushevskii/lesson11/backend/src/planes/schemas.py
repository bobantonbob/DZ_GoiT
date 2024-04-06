import pydantic

class PlaneResponseSchema(pydantic.BaseModel):
    id: int
    model: str
    image_url: str
    fuel_tank_volume: int
