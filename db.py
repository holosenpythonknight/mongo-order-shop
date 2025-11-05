import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

db_url = os.getenv("DATABASE_URL")

if not db_url:
    raise RuntimeError("DATABASE_URL is not set in .env")

client = MongoClient(db_url)
db = client.get_database()


def get_db():
    return db
