# liste = ["1","2","5a","10b","abc"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# while True:
#     sayi = input("Sayı: ")
#     if sayi == "q":
#         break 
#     try:
#         result = float(sayi)
#         print("Sayı başarılı : ",result)
#         break
#     except ValueError:
#         print("geçersiz sayı")
#         continue   

# def checkPass(parola):
#     turkce_chars = "şçğüöıİ"

#     for i in parola:
#         if i in turkce_chars:
#             raise TypeError("Parola Türkçe karakter içeremez!")
#         else:
#             pass

#     print("geçerli parola")

# parola = input("Parola: ")

# try:
#     checkPass(parola)
# except TypeError as ex:
#     print(ex)


def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif değer")

    result = 1

    for i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20 , -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as ex:
        print(ex)
        continue

    print(y)

