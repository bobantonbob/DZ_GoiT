from typing import Any, Iterable
from table import Table
from dataclasses import dataclass

@dataclass
class Car:
    id: int
    brand: str
    model: str

class CarTable(Table):
    def __init__(self):
        super().__init__("cars",
            {
                "id": "integer PRIMARY KEY NOT NULL",
                "brand": "varchar(255) NOT NULL",
                "model": " varchar(255) NOT NULL"
            },
            []
        )

    def create(self, car: Car) -> int | None:
        return super().create(car.__dict__)

    def get_all(self) -> list[Car] | None:
        result = []
        rows = super().get_all()

        for i in rows:
            result.append(Car(*i))
        
        return result

    def update(self, car: Car, **kwargs):
        super().update(car.__dict__, kwargs)