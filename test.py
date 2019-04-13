import numpy as np
from numpy import *
import matplotlib.pyplot as plt


points = np.DataIn = loadtxt('punkty_sorted.txt')
point1 = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])
# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial
z = np.polyfit(x, y, 5)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
#plt.xlim([x[0]-1, x[-1] + 1 ])

plt.show()