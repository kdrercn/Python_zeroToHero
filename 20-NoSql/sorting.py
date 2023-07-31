import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]


# result = mycollection.find().sort('price', -1)
result = mycollection.find().sort([("name",1), ("price",-1)])

for i in result:
    print(i)

