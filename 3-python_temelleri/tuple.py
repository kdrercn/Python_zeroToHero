list = [1,2,3]
tuple = (1,"iki", 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ["ali","veli"]
tuple = ("damla","ayşe")
names = ("demet","emel","ayşe") + tuple #toplama da oluyor

# list[0] ="ahmet"
# tuple[0] = "deniz" #tuple'a eleman ekleyemiyoruz

print(tuple.count("damla"))
print(tuple.index("ayşe")) #sadece bu iki fonk. kullanılıyor

print(names)
print(list)
print(tuple)