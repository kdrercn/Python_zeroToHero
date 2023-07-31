# # encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)
# # inner_increment sadece outerın içinde çalışır.
# outer(10)

def factorial(num):
    if not isinstance(num, int):
        raise TypeError("Sayı olmalı")

    if not num >= 0:
        raise ValueError("Sayı 0 ya da pozitif olmalı")

    def inner_facto(num):
        if num <= 1:
            return 1
        
        return num * inner_facto(num -1)

    return inner_facto(num)
try:
    print(factorial("a"))
except Exception as ex:
    print(ex)
