araba=["Bmw","Mercedes","Opel","Mazda"]

# print(len(araba)) #liste eleman sayısı

# print(araba[0]+" "+araba[-1]) #listenin ilk ve son eleman

# araba[3]="Toyota" #mazdayı toyotayla değiştir

# x=araba.index("Mercedes")
# result="Mercedes" in araba
# print(result) #2 yollu mercedes var mı

# print(araba[-2]) #-2. eleman

#print(araba[0:3]) #ilk 3 elemanı yazdır

# arabalar[-2:]=["Toyota","Renault"] #son 2 elemanı değiştir

# araba.insert(4,"Audi")
# araba.insert(5,"Nissan")
# result = araba + ["Audi" + "Nissan"] #audi ve nissan ekle

# araba.remove(araba[3])
# del araba[-1] #son elemanı sil

# araba.sort(reverse=True)
# result = araba[::-1] #Tersten yaz

studentA=["Yiğit", "Bilgi", 2000,[70,60,70]]
studentB=["Sena", "Turan", 1999,[80,80,70]]
studentC=["Ahmet", "Turan" ,1998,[80,70,90]]
students = [studentA, studentB,studentC]

result = studentA[0]
result = f"{studentA[0]} {studentA[1]}  {2020 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
# print(araba)
# print(students)