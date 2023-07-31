import pymongo

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]

# result = mycollection.find_one()

for i in mycollection.find({},{"_id":0}):
    print(i)
# print(result)