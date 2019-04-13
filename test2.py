import matplotlib.pyplot as plt 
from scipy import stats
import numpy as np
from numpy import *

points = np.DataIn = loadtxt('punkty1.txt')
x = points[:,0]
y = points[:,1]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f" % (slope, intercept))
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + (slope*x), 'r', label='fitted line')
plt.legend()
plt.show()