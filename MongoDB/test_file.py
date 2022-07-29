from mongoDBmanagement import MongoDBManagement

mydb = MongoDBManagement('root', 'root')

client = mydb.getMongoDBClientObject()

d = {
    "name":"Abhishek",
    "email":"kashyapabhishek22@gmail.com",
    "surname":"Kumar"
}

db1 = client['mongotest']
coll = db1['Test']
coll.insert_one(d)


