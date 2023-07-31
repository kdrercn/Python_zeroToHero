import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z =  x ** 2

'''
figure = plt.figure()

axes = figure.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,"b")
axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_title("Cube")

axes2 = figure.add_axes([0.15,0.6,0.25,0.25])
axes2.plot(x,z,"r")
axes2.set_xlabel("X")
axes2.set_ylabel("Y")
axes2.set_title("Square")

'''

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cubic")
axes.legend(loc=1) # 1=sağ üst 2=sol üst 3=sol alt 4=sağ alt

'''
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.pdf")
'''

plt.show()
