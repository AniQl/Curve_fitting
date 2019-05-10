import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from scipy import interpolate
from scipy.interpolate import InterpolatedUnivariateSpline

points = np.DataIn = loadtxt('punkty_sorted.txt')

x = points[:,0]
y = points[:,1]
n = len(x)

spl = InterpolatedUnivariateSpline(x, y)
plt.plot(x, y, 'g-', ms=5, label='original')
xs = np.linspace(x[0], x[-1], 50)
plt.plot(xs, spl(xs), 'r', lw=3, alpha=0.7, label='interpolated')
plt.legend(loc='best')
plt.show()
