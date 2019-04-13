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
plt.plot(x, y, 'ro', ms=5)
xs = np.linspace(x[0], x[-1], 50)
plt.plot(xs, spl(xs), 'g', lw=3, alpha=0.7)
plt.show()

