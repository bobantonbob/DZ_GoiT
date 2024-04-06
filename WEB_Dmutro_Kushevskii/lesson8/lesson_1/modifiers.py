import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

database = client.main_db

res = database.users.find({"positions": {"$exists": True}})
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({"name": {"$type": "string"}})
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({"name": {"$regex": "o"}})
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({"$or": [{"name": "Dima"}, {"age": {"$exists": True}}]})
for val in res:
    print(val)
