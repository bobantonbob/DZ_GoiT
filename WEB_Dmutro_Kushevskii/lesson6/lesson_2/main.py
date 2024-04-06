import sqlite3
import logging
import faker

from table import Table
from car_table import CarTable, Car
from car_photo_table import CarPhotoTable, CarPhoto

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    'line_num: %(lineno)s > %(message)s'
)

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def generate_fake_cars(car_table, amount, start_id):
    fake_data = faker.Faker()

    for i in range(start_id, start_id + amount):
        car_table.create(
            Car(
                i, fake_data.company(), fake_data.name()
            )
        )

def main():
    with sqlite3.connect("test.sqlite") as conn:
        Table.conn = conn

        car_table = CarTable()
        car_photo_table = CarPhotoTable()

        # logging.debug(car_table.create(Car(1, "daewoo", "lanos")))
        # logging.debug(car_table.create(Car(2, "mercedes", "S")))
        # logging.debug(car_table.create(Car(3, "Skoda", "Super B")))

        # my_car_photo = CarPhoto(1, "https://a.d-cd.net/a7a5852s-960.jpg", 1)

        # logging.debug(car_table.get_all())
        # car_table.update(Car(id=None, brand="Tesla", model=None), id=2)
        # logging.debug(car_table.get_all())
        # car_table.remove({"id": 2})
        logging.debug(car_table.get_all())
        generate_fake_cars(car_table, 5, 4)
        logging.debug(car_table.get_all())



if __name__ == "__main__":
    main()
