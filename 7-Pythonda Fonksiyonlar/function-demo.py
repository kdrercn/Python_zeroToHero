# Gönderilen kelimeyi istenen sayıda yazdıran fonk
# def yazdir(kelime, adet):
#     print(kelime * adet)

# yazdir('Merhaba\n', 10)

#ben
# def repeater(word, time):
#     a = 0
#     while a < time:
#         print(word)
#         a += 1

# kelime = input("Kelimeyi giriniz: ")
# sayi = int(input("Kaç kez tekrarlansın: "))

# repeater(kelime, sayi)


#Sınırsız parametreyi listeye çevir
# def listeyeCevir(*params):
#     liste = []

#     for param in params:
#         liste.append(param)

#     return liste

# result = listeyeCevir(10,20,30,'Merhaba')

# print(result)

#ben
# def listMaker(things):
#    list.append(things)
    
# list = []

# while True:
#     x = input("Eklenecek değer: ")
#     listMaker(x)
#     print(list)

# aralıktaki asal değerleri bul
# def asalBul(num1, num2):
    
#     for x in range(num1, num2):
#         asalmi = True
#         if x == 1:
#             asalmi = False
#         for i in range(2, x):
#             if (x % i == 0):
#                 asalmi = False
#                 break
#         if asalmi:
#             print(x)
        

# asalBul(2,10)

# Gönderilen sayının tam bölenlerini liste olarak verir
# def bolenler(num):
#     list = []
#     for x in range(1,num + 1):
#         if(num % x == 0):
#             list.append(x)
#     print(list)


# bolenler(1000)