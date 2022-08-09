import pymongo

if __name__ == "__main__":
    print("Hello World. Welcome to PyMongo");

    client = pymongo.MongoClient("mongodb://localhost:27017");
    #  Verify client connection
    print(client);

    database = client['Sample'];
    collection = database['Sample Collection'];

    users = collection.find({"Name" : "Ishaan"} , {"Intern" : 0 , "_id" : 0});
    
    for user in users:
        print(user);
