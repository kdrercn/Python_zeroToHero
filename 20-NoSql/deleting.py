import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]

for i in mycollection.find():
    print(i)

print("*"*50)

# mycollection.delete_one({"name": "Samsung S7"})
# mycollection.delete_many({"name": "Samsung S7"})




for i in mycollection.find():
    print(i)
