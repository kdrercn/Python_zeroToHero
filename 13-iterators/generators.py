# bellekte yer işgal etmeyen bir iterator anlık kullanım için

# def cube():
#     for i in range(5):
#         yield i ** 3

# for i in cube():
#     print(i)

gen = (i**3 for i in range(5))

for i in gen:
    print(i)