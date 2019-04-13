import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from scipy import interpolate
from sympy import Integer, Float

points = np.DataIn = loadtxt('punkty1.txt')

x = points[:,0]
y = points[:,1]
n = len(x)

print(x,y)

tck, u = interpolate.splprep([x,y],k=3,s=0)
u = np.linspace(0,1,num=50,endpoint=True)
out = interpolate.splev(u,tck)

plt.figure()
plt.plot(x, y, 'ro', out[0], out[1], 'b')
plt.legend(['Points', 'Interpolated B-spline', 'True'],loc='best')
plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
plt.title('B-Spline interpolation')
plt.show()