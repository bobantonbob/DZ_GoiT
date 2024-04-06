from table import Table
from dataclasses import dataclass

@dataclass
class CarPhoto:
    id: int
    photo_url: str
    car_id_fn: int


class CarPhotoTable(Table):
    def __init__(self):
        super().__init__("photos",
            {
                "id": "integer PRIMARY KEY NOT NULL",
                "photo_url": "varchar(255) NOT NULL",
                "car_id_fn": "integer"
            },
            [
                "FOREIGN KEY(car_id_fn) REFERENCES car(id)"
            ]
        )

    def create(self, car_photo: CarPhoto) -> int | None:
        return super().create(car_photo.__dict__)

    def get_all(self) -> list[CarPhoto] | None:
        result = []
        rows = super().get_all()

        for i in rows:
            result.append(CarPhoto(*i))
        
        return result

    def update(self, car_photo: CarPhoto, **kwargs):
        super().update(car_photo.__dict__, kwargs)
