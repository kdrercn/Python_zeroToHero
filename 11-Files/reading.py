# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya bulunamadı")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file = open("newfile.txt","r",encoding="utf-8")

# w/for
# for i in file:
#     print(i, end="")

###########################################

# # w/read fonksiyonu
# content1 = file.read()
# print("içerik 1")
# print(content1)
# #2. content yazmama sebebi ilk contenti kapamadığımız için cursor orada kalır ve okumaya oradan devam eder.
# file = open("newfile.txt","r",encoding="utf-8")
# content2 = file.read()
# print("içerik 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# print(content)

###########################################

# readline fonksiyonu //her satırı tek tek okur

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

###########################################

# readlines fonksiyonu //her satırı dizi elemanı olarak atar

# liste = file.readlines()
# print(liste[0])

file.close()