import numpy as np
from numpy import *
import matplotlib.pyplot as plt

points = np.DataIn = loadtxt('punkty_sorted.txt')
x = points[:,0]
y = points[:,1]

z = np.polyfit(x, y, 6)
z1 = np.polyfit(x, y, 3)
f = np.poly1d(z)
f1 = np.poly1d(z1)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

x1_new = np.linspace(x[0],x[-1], 50)
y1_new = f1(x1_new)

plt.plot(x, y , 'o', label='original')
plt.plot(x_new, y_new, '-', label='6th degree')
plt.plot(x1_new, y1_new, '-', label='3th degree')
plt.legend(loc='best')
plt.show()
