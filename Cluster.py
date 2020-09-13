import os
from dotenv import load_dotenv

import pymongo
from pymongo import MongoClient

load_dotenv()

db_cluster=os.getenv('db_cluster')

#MongoDB cluster
cluster = MongoClient(db_cluster)
db = cluster["bot_user_data"]
collection = db["bot_user"]
