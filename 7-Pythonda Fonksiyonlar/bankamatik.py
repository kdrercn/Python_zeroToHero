hesapKadir = {
    'ad': 'Kadir Ercen',
    'hesapNo': '123456',
    'bakiye': 3000,
    'ekHesap': 2000
}
hesapSude = {
    'ad': 'Sude Ercen',
    'hesapNo': '123457',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print('Paranızı alabilirsiniz')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanılsın mı (e/h): ')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                bakiyeSorgula(hesap)
        else:
            print('Bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır. Ek hesap bakiyenizde ise {hesap["ekHesap"]} TL bulunmaktadır.')

paraCek(hesapKadir, 3000)
# bakiyeSorgula(hesapKadir)
print("***************")
paraCek(hesapKadir, 2000)
# bakiyeSorgula(hesapKadir)