import pymongo

client = pymongo.MongoClient("mongodb+srv://test:root@cluster0.ne0ebrv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Abhishek",
    "email":"kashyapabhishek22@gmail.com",
    "surname":"Kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)