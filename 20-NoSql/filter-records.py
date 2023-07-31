import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]

# filter = {"name": "Samsung S5"}
# result = mycollection.find(filter)

# result = mycollection.find_one({"_id": ObjectId("5f5f29998a08b2d5fe7ca6a1")})


# result = mycollection.find({
#     "name": {
#         "$in" : ["Samsung S5","Samsung S6"]
#     }
# })

# gt büyük, lt küçük olan
# result = mycollection.find({
#     "price": {
#         "$gt" : 4000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$gte" : 4000
#     }
# })

# result = mycollection.find({
#     "price": {
#         "$eq" : 4000
#     }
# })

# result = mycollection.find({
#     "price": 4000
    
# })

# https://docs.mongodb.com/manual/reference/operator/query/

#regular expression
# result = mycollection.find({
#     "name": { "$regex": "^S" }
# })


for i in result:
    print(i)
# print(result)

