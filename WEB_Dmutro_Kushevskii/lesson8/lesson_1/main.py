import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])
