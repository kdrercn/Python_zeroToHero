# bir kaç yerde kullanmak istediğimiz fonksiyonu bir çok fonk ile bağdaştırmak

# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayGreeting(name):
#     print("greeting", name)

# sayGreeting("Kadir")

import math
import time

def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
       
        func(*args,**kwargs)
       
        finish = time.time()
        print("Fonksiyon "+func.__name__+ " " + str(finish-start)+ " saniye sürdü.")
    return inner

@calculateTime
def usalma(a,b):
    print(math.pow(a,b))
@calculateTime
def fakto(num):
    print(math.factorial(num))
@calculateTime
def topla(a,b,c):
    print(a+b+c)

usalma(2,3)
fakto(4)
topla(10,20,30)
