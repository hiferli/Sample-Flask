import pymongo

if __name__ == "__main__":
    print("Hello World. Welcome to PyMongo");

    client = pymongo.MongoClient("mongodb://localhost:27017");
    collection = client['Sample'];

    previous_data = {"Name" : "Ramen"};
    next_data = {"$set" : {"Intern" : True}};

    collection.update_one(previous_data , next_data);