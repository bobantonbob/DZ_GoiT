import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

database = client.main_db

database.users.insert_one(
    {
        "name": "Antony",
        "positions": ["Engineer", "Lecturer"],
        "best_friend": {"name": "Josh"},
        "friends": [{"name": "Josh"}, {"name": "Bob"}]
    }
)

res = database.users.find_one({"best_friend.name": "Josh"})
print(res)

print("---------------------------------------------")

res = database.users.find_one({"friends": {"$elemMatch": {"name": "Bob"}}})
print(res)

print("---------------------------------------------")

database.users.insert_one(
    {
        "name": "Rob",
        "age": 28
    }
)

res = database.users.find({"age": {"$gt": 20}}) # gte;lte;gt;lt;eq
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({}).skip(2)
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({}).limit(1)
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.find({}).sort({"name": -1}).limit(1)
for val in res:
    print(val)

print("---------------------------------------------")

res = database.users.count_documents({})
print(res)
