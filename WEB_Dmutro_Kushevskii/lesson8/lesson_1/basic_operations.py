import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

client.drop_database("main_db")

database = client.main_db
database.users.insert_one(
    {"name": "Dima", "positions": ["Engineer", "Lecturer"]}
)

print("---------------------------------------------")

res = database.users.find({}, {"_id": 0})
for val in res:
    print(val)
