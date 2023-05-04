import os
from dotenv import load_dotenv

from util import mongodb

load_dotenv()

def main():
    db = mongodb.DB('ReviewChat')
    collection = db.get_collection('tourism')
    item_1 = {
        "item_name" : "Blender",
        "item_price" : 100,
        "item_quantity" : 10
    }
    # collection.insert_one(item_1)
    # data = collection.find_one({'item_name' : 'Blender'}, {'_id': 1})
    # print(data)


if __name__ == "__main__":
    main()