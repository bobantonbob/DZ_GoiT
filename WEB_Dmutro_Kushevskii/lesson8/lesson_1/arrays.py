import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

collection = client.main_db.users

# res = collection.find({})
# for val in res:
#     print(val)

# collection.insert_one({
#     "name": "Weirdo", "age": [28, 33]
# })

# res = collection.find({"age": {"$in": [28, 33]}})
# for val in res:
#     print(val)

# res = collection.find({
#     "$and": [
#         {"age": {"$nin": [33, 36]}},
#         {"age": {"$exists": True}},
#     ]
# })
# for val in res:
#     print(val)

# res = collection.find({"age": {"$all": [28, 33]}})
# for val in res:
#     print(val)

# res = collection.find({"friends": {"$size": 3}})
# for val in res:
#     print(val)

# res = collection.update_many(
#     {
#         "name": "Antony"
#     },
#     {
#         "$push": {
#             "friends": {"name": "Arnold"}
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)

# res = collection.update_many(
#     {
#         "name": "Antony"
#     },
#     {
#         "$push": {
#             "friends": {
#                 "$each": [{"name": "Oleksandr"}, {"name": "Iurii"}]
#             }
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)

# res = collection.update_many(
#     {
#         "name": "Antony"
#     },
#     {
#         "$addToSet": {
#             "friends": {"name": "Kostioantyn"}
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)

# res = collection.update_one(
#     {
#         "name": "Antony"
#     },
#     {
#         "$pop": {
#             "friends": -1
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)

# res = collection.update_many(
#     {
#         "name": "Antony"
#     },
#     {
#         "$pull": {
#             "friends": {"name": "Arnold"}
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)

# res = collection.update_many(
#     {
#         "name": "Antony"
#     },
#     {
#         "$pullAll": {
#             "friends": [{'name': 'Bob'}, {'name': 'Josh'}]
#         }
#     })

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)


# res = collection.update_many(
#     {"name": "Antony"},
#     {
#         "$push": {
#             "friends": {
#                 "$each": ["Bob", "Josh"]
#             }
#         }
#     }
# )

# res = collection.find({"name": "Antony"})
# for val in res:
#     print(val)
