import pymongo

if __name__ == "__main__":
    print("Hello World. Welcome to PyMongo");

    client = pymongo.MongoClient("mongodb://localhost:27017");
    database = client['Sample']
    collection = database['Sample Collection'];

    deleteData = {"Name" : "Joshi"};

    count = collection.delete_many(deleteData);
    print(count.deleted_count);