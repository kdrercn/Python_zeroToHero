fruits = {'orange','apple','banana'}

# print(fruits[0]) #indekslenemez, sıralanamaz

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple']) #apple zaten olduğu içiin eklenmez

fruits.remove('mango')
fruits.discard('apple')
fruits.pop() #normal listede son eleman silinir ama burada rastgele siler
fruits.clear()
print(fruits)

myList = [1,2,5,4,4,2,1]

print(myList)
print(set(myList))