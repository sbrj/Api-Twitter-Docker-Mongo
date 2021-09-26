from pymongo import MongoClient

client = MongoClient("mongodb://dio:dio@localhost:27017/")

db = client.testando
print('apos db')
collection = db.test_collection

print('antes autor')
post = {"autor": "jorge", "texto": "texto"}

posts = db.posts

post_id = posts.insert_one(post).inserted_id

post_id

db.list_collection_names()

import pprint
pprint.pprint(posts.find_one())