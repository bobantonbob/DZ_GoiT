from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb://localhost')

    db = client.dz10

    return db
