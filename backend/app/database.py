from pymongo import MongoClient
from app.config import settings

client = MongoClient(settings.MONGO_URL)
db = client["testdb"]
collection = db["items"]