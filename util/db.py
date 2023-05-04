import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
MONGODB_PW = os.environ.get('MONGODB_PASSWORD')

CONNECTION_STRING = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PW}@cluster0.xza4gbz.mongodb.net/?retryWrites=true&w=majority"

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
#   "category" : "kitchen appliance"
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