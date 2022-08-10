import pymongo

if __name__ == "__main__":
    print("Hello World. Welcome to PyMongo");

    client = pymongo.MongoClient("mongodb://localhost:27017");
    database = client['Sample']
    collection = database['Sample Collection'];


    previous_data = {"Name" : "Ishaan"};
    next_data = {"$set" : {"Name" : "Joshi"}};

    collection.update_many(previous_data , next_data);