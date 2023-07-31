import matplotlib.pyplot as plt
import numpy as np

"""
# Stack Plot
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]



plt.plot([],[],color = "y", label = "oyuncu1")
plt.plot([],[],color = "r", label = "oyuncu2")
plt.plot([],[],color = "b", label = "oyuncu3")

plt.stackplot(yil, oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Goller")
plt.xlabel("Yıl")
plt.ylabel("Gol")
"""

"""
# Pie Grafik

goal_types = "Penaltı","Kaleye Atılan Şut","Serbest Vuruş"

goals = [12,35,7]
colors = ["y","r","b"]
plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
"""

"""
# Bar Grafiği

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
"""

"""
# Histogram Grafik

yaslar = np.random.randint(1,100,50)
yas_gruplari = np.linspace(0,100,11)

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("Yaş grupları")
plt.ylabel("Kişi sayısı")
plt.title("Histogram")
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 11, 1)) 
"""

plt.show()