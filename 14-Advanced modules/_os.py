import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör") # iç içe
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir() # etkin olan dizindeki klasörleri gösterir
# result = os.listdir('C:\\') # C dizinindeki tüm klasörler
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py") 
# result = result.st_size/1024 # dosya boyutu KB türünde
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe") # dosya açar

# path

result = os.path.abspath("_os.py") # tam konum
result = os.path.dirname("C:/python/advanced-modules/_os.py") # dosyanın dizin ismi
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/python/advanced-modules/_os1.py") # bu konumda dosya
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules") # klasör
result = os.path.isfile("C:/python/advanced-modules/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)