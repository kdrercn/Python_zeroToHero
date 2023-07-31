import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]

# ilk s6 iphone 7
# mycollection.update_one(
#     {"name": "Samsung S6"},
#     {"$set": {
#         "name": "Iphone 7",
#         "price": 7000
#     }}
# )

# tüm s6lar iphone 7
mycollection.update_many(
    {"name": "Samsung S6"},
    {"$set": {
        "name": "Iphone 7",
        "price": 7000
    }}
)


for i in mycollection.find():
    print(i)