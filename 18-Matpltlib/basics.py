import matplotlib.pyplot as plt
import numpy as np

'''
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r") # matplotlib plot style google marker-çizgi tipi-renk

plt.axis([0,6,0,20]) # tablonun aralığı için ilk 2 x için
plt.title("Grafik Başlığı")
plt.xlabel("X")
plt.ylabel("Y")
'''
'''
x = np.linspace(0,2,100)
plt.plot(x, x, label="lineer")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple plot")

plt.legend()
plt.show()
'''


'''
axs[0].plot(x,x,color="red")
axs[0].set_title("linear")
axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("cubic")
plt.tight_layout()

'''
'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("Başlık")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")
'''

import pandas as pd

df = pd.read_csv("Films.csv")
# df = df.drop(["Directors"], axis = 1).groupby("Your Rating").mean()
# df.plot(subplots=True)
# plt.legend()


# plt.show()

result = df.head(10)
print(result)