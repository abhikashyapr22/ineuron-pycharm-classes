import pymongo
import ssl

ssl_cert_reqs = ssl.CERT_NONE

client = pymongo.MongoClient("mongodb+srv://snshrivas:Snshrivas1995@cluster0.u46c4.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

database = client['myinfo']
collection = database['Abhi']

data = {
    "name": "Abhishek",
    "mail_id": "kashyapabhishek22@gmail.com",
    "subject": ["FSDS", "big data", "data analytics"]
}

collection.insert_one(data)

# data = collection.find({"companyName": "ineuron"})
# data = collection.find({"courseOffered": {"$gt": "E"}})
#
# for i in data:
#     print(i)
