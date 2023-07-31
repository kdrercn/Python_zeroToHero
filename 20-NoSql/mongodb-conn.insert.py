import pymongo

myclient = pymongo.MongoClient("mongodb+srv://kdrercn:XO3cnkWt2ZiBQAOI@cluster0.d0e7e.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb["prducts"]

# product = {"name":"Samsung S5", "price":2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(mydb.list_collection_names())

# print(myclient.list_database_names())

productList = [
    {"_id":1,"name":"Samsung S6", "price":3000, "description": "dandik"},
    {"_id":2,"name":"Samsung S7", "price":4000, "categories":['telefon','elektronik']}
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)