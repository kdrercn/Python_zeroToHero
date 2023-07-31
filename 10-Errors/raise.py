# x = 10 

# if x > 5:
#     raise Exception("x 5den büyük olamaz")

# def check_pass(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 7 karakterli olmalıdır!")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Parola küçük harf içermelidir!")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Parola büyük harf içermelidir!")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Parola rakam içermelidir!")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Parola alfa numerik karakter içermelidir!")
#     elif re.search("\s",psw):
#         raise Exception("Parola boşluk içermemelidir!")
#     else:
#         print("Geçerli parola")

# password = "12345678aA_"

# try:
#     check_pass(password)
# except Exception as ex:
#     print(ex)



# class Person:
#     def __init__(self, name, year):
#         if len(name) > 10:
#             raise Exception("Name alanı fazla karakter içeriyor.")
#         else:
#             self.name = name

# p = Person("Kadirrrrrrr",2000)