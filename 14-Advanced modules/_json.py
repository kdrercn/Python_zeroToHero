import json

personStr = '{"name":"Kadir", "languages":["python","C#"]}'

personDict = '{"name": "Ali", "languages": ["Python","C#"]}'

# # JSON str to dict
# result = json.loads(personStr)

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])


# Dict to JSON str
# result = json.dumps(personDict)
# print(result)

# with open("person.json","w") as f:
#     json.dump(personDict, f)

personDict = json.loads(personStr)

result = json.dumps(personDict, indent=4, sort_keys= True)
print(personDict)
print(result)