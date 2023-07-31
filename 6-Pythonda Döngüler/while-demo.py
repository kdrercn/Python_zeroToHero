

# sayilar = [1,3,5,7,9,12,19,21]

# x=0
# while x < len(sayilar):
#     print(sayilar[x])
#     x+=1

# bas = int(input("Başlangıç: "))
# son = int(input("Bitiş: "))
# i = bas
# while i < son:
#     i+=1
#     if(i % 2 != 0):
#         print(i)
#    

# a=100
# while a >= 1:
#     print(a)
#     a -= 1

# numbers = []
# i = 0
# while i<5:
#     sayi = int(input('sayı: '))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)
    
urunler = []
adet = int(input('kaç tane: '))
i = 0
while(i<adet):
    name = input('ürün ismi: ')
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']} ürün fiyatı: {urun['price']}")  
