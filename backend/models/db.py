import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# Use default DB from connection string
db = client.get_database()

# EXPORTED COLLECTIONS
user_collection = db["users"]
company_collection = db["companies"]
