import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
MONGODB_PW = os.environ.get('MONGODB_PASSWORD')

CONNECTION_STRING = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PW}@cluster0.xza4gbz.mongodb.net/?retryWrites=true&w=majority"

class DB:
    def __init__(self, db):
        self.db_name = db
        self.db = MongoClient(CONNECTION_STRING)[db]
    def get_collection(self, collection):
        return self.db[collection]
    def insert(self, collection, item):
        self.db[collection].insert_one(item)
    def insert_many(self, collection, items):
        self.db[collection].insert_many(items)
    def find_all(self, collection):
        return self.db[collection].find()
    def find_all_sorted(self, collection, sort_key, sort_order):
        return self.db[collection].find().sort(sort_key, sort_order)
    def find_all_sorted_limit(self, collection, sort_key, sort_order, limit):
        return self.db[collection].find().sort(sort_key, sort_order).limit(limit)
    def find_all_sorted_limit_skip(self, collection, sort_key, sort_order, limit, skip):
        return self.db[collection].find().sort(sort_key, sort_order).limit(limit).skip(skip)
    def find(self, collection, query):
        return self.db[collection].find(query)
    def find_one(self, collection, query):
        return self.db[collection].find_one(query)
    def update(self, collection, query, update):
        self.db[collection].update_one(query, update)
    def delete(self, collection, query):
        self.db[collection].delete_one(query)
    def delete_many(self, collection, query):
        self.db[collection].delete_many(query)
    def drop(self, collection):
        self.db[collection].drop()
    def drop_db(self):
        self.db.drop()

        
def get_db(name):
    client = MongoClient(CONNECTION_STRING)
    
    # Create the database for our example (we will use the same database throughout the tutorial
    return client[name]

def get_collection(db, name):
    return db[name]

def main():
    ca_db = get_db('ChatAssistant')
    collection = get_collection(ca_db, 'tourism')
    item_1 = {
        "_id" : "U1IT00001",
        "item_name" : "Blender",
        "max_discount" : "10%",
        "batch_number" : "RR450020FRG",
        "price" : 340,
        "category" : "kitchen appliance"
    }

    item_2 = {
        "_id" : "U1IT00002",
        "item_name" : "Egg",
        "category" : "food",
        "quantity" : 12,
        "price" : 36,
        "item_description" : "brown country eggs"
    }
    collection.insert_many([item_1,item_2])
    print('done')

if __name__ == "__main__":
    main()

# Insert example
# item_1 = {
#   "_id" : "U1IT00001",
#   "item_name" : "Blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340,
#   "category" : "kitchen appliance",
    # comments: [
    #     {
    #         user: 'user1',
    #         message: 'My first comment',
    #         dateCreated: new Date(2011,1,20,2,15),
    #         like: 0
    #     },
    #     {
    #         user: 'user2',
    #         message: 'My second comments',
    #         dateCreated: new Date(2011,1,25,7,45),
    #         like: 5
    #     }
    # ]
# }

# item_2 = {
#   "_id" : "U1IT00002",
#   "item_name" : "Egg",
#   "category" : "food",
#   "quantity" : 12,
#   "price" : 36,
#   "item_description" : "brown country eggs"
# }
# collection_name.insert_many([item_1,item_2])

# Find example
# item_details = collection_name.find()
# for item in item_details:
#    # This does not give a very readable output
#    print(item)
#    print(item['item_name'], item['category'])