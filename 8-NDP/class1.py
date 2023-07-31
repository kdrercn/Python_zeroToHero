class Circle:
    pi = 3.14

    def __init__(self, r = 1):
        self.r = r
    
    def cevreHesapla(self):
        return 2*self.pi*self.r

    def alanHesapla(self):
        return self.pi*self.r*self.r

c1 = Circle() # r = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alanHesapla()} çevre = {c1.cevreHesapla()}')
print(f'c2 : alan = {c2.alanHesapla()} çevre = {c2.cevreHesapla()}')
