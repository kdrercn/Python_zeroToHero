def notHesap(satir):
    satir = satir[:-1] #boşlukları yok eder
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1+not2+not3)/3

    return ogrenciAdi + ": " + str(ort) + "\n"

def ortOku():
    with open("sinavNot.txt","r",encoding="utf-8") as file: 
        for satir in file:
            print(notHesap(satir))

def notGir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("1. Not: ")
    not2 = input("2. Not: ")
    not3 = input("3. Not: ")

    with open("sinavNot.txt","a",encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")

def notKayit():
    with open("sinavNot.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(notHesap(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortOku()
    elif islem == "2":
        notGir()
    elif islem == "3":
        notKayit()
    else:
        break