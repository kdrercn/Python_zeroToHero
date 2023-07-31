# def say(name):
#     print('Hello ' + name)
   
# isim = input("İsim giriniz: ")
# say(isim)



# def total(num1, num2):
#     return num1 + num2

# sayi1 = int(input("İlk sayıyı giriniz: "))
# sayi2 = int(input("İkinci sayıyı giriniz: "))
# result = total(sayi1,sayi2)
# print(result)

import datetime
year = datetime.date.today().year

def yasHesapla(dogumYili):
    return year - dogumYili

# yil = int(input("Hangi yılda doğdunuz: "))
# x = yasHesapla(yil)
# print(x)

def yearToRetirement(dogumYili, isim):
    '''
    DOCSTRING: Dogum yilina gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Emeklilik yili
    '''
    yas = yasHesapla(dogumYili)
    retirement = 65 - yas
    
    if retirement > 0:
        print(f'Sayın {isim}, Emekliliğinize {retirement} yıl kaldı. ')
    else:
        print('Sayın {isim}, Zaten emeklisiniz.')

yearToRetirement(1972, 'Kadir')
print(help(yearToRetirement))