'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

sayi = int(input('sayı: '))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayı asaldır.')
else:
    print('sayı asal değildir.')





# #ben

# sayi = int(input("Sayi: "))
# asalMi = True


# if(sayi == 1):
#     asalMi = False

# for x in range(2,sayi):
#     if(sayi % x == 0):
#         asalMi = False
#         break

# if asalMi:
#     print(f"{sayi} asaldır.")
# else:
#     print(f"{sayi} asal değil. ")










