import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

database = client.main_db

database.users.update_one({"name": "Lili"}, {"$set": {"name": "Lili", "age": 29}}, upsert=True)
res = database.users.find_one({"name": "Lili"})
print(res)

print("---------------------------------------------")

database.users.update_one({"name": "Lili"}, {"$set": {"age": 30}})
res = database.users.find_one({"name": "Lili"})
print(res)

print("---------------------------------------------")

database.users.update_one({"name": "Lili"}, {"$unset": {"age": 1}})
res = database.users.find_one({"name": "Lili"})
print(res)

print("---------------------------------------------")

database.users.delete_one({"name": "Lili"})
res = database.users.find_one({"name": "Lili"})
print(res)
