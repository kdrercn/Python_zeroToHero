# value
# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)

# reference
# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# n = sehirler[:]
# n[0] = 'istanbul'
# this dud makes slicing

# change(sehirler[:]) #orjinal liste değişmemiş olur
# print(sehirler)
# print(n)


# def add(*params):
#     return sum((params))

# print(add(10,20))

# def displayUser(**args):
#     for key, value in args.items():
#         print(f'{key} is {value}')
        
# displayUser(name = 'Kadir', age = 20, city = 'Gönen')
# displayUser(name = 'Sude', age = 17, city = 'Gönen', phone = '2131232')
# displayUser(name = 'Zeynep', age = 9, city = 'Gönen', phone = '2323123', email = 'sude@gmail.com')

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value 2')

