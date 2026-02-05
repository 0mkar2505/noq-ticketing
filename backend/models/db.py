from pymongo import MongoClient
import certifi
import os

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

db = client["noq_db"]

user_collection = db["users"]
company_collection = db["companies"]
