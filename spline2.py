import numpy as np
import matplotlib.pyplot as plt
from numpy import *

#x = np.array([-4,-2,0,2,4,7])
#y = np.array([-128,-16,0,-40,16,51])

points = np.DataIn = loadtxt('punkty1.txt')
  
  # get x and y vectors
x = points[:,0]
y = points[:,1]
n = len(x)

print("\nx =",x)
print("\ny = ",y)

h = np.array(x[1:n]-x[0:n-1])
print("\nh =",h)

b = np.divide(y[1:n]-y[0:n-1],h)
print("\nb = ",b)

m = len(h)

# To determine z0,z1,...,zn, we need to solve a system of equations
# For natural splines, z0 = zn = 0. 
# So, we can eliminate the first and last columns. 
# The result is a (n-1)x(n-1) square matrix

s = (n-2,n-1)
p = n-2
q = n-1
A = np.zeros(s)

if s == (1,2):
    A[0][0]=2*(h[0]+h[1])
    A[0][1]=6*(b[1]-b[0])
    
if s == (2,3):
    A[0][0]=2*(h[0]+h[1])
    A[0][1]=h[1]
    A[1][0]=h[1]
    A[1][1]=2*(h[1]+h[2])
    
    A[0][2]=6*(b[1]-b[0])
    A[1][2]=6*(b[2]-b[1])

if (n-2) > 2:
    A[0][0]=2*(h[0]+h[1])
    A[0][1]=h[1]
    A[p-1][q-3]=h[m-2]
    A[p-1][q-2]=2*(h[m-2]+h[m-1])
    
    A[0][q-1]=6*(b[1]-b[0])
#    A[p-1][q-1]=6*(b[m-1]-b[m-2])
    A[p-1][q-1]=6*(b[m-2]-b[m-3])
    
    for i in range(1,p-1):
        A[i][i-1]= h[i]
        A[i][i]= 2*(h[i]+h[i+1])
        A[i][i+1]=h[i+1]
        
        A[i][q-1] = 6*(b[i+1]-b[i])
        
print("\nThe linear system of equations to be solved is : \n")    
print(A)

#======

# The augmented matrix is A
(r,t) = np.shape(A)

if(r,t) == (1,2):
    z = A[0][1]/A[0][0]

if r > 1:
    for i in range(0,r):
        pivot = A[i][i]
    
        for j in range(i+1,r):
            # Find the multiplier
            l = (A[j][i]/pivot)
        
            for k in range(i,t):
                A[j][k] = A[j][k]-(l*A[i][k])

    # The resulting upper triangular matrix
    print("\nThe resulting upper triangular matrix is : \n")    
    print(A)

    z = A[:,t-1]

    for i in range(r-1,-1,-1):
        for j in range(r-1,i,-1):
            z[i] = z[i]-(A[i][j]*z[j])

        z[i]=z[i]/A[i][i]
        A[i][t-1] = z[i]

z = np.append(np.array([0]),z)
z = np.append(z,0)

# After gaussian elimination, the values of z1,...,zn-1 are    
print("\nAfter gaussian elimination, the values of z1,...,zn-1 are")
print("\n",z)

#====

# Compute the coefficients a[i], b[i], c[i] and c[i]
n = len(x)-1

e = np.zeros(n)
f = np.zeros(n)
g = np.zeros(n)
o = np.zeros(n)

for i in range(0,n-1):
    e[i]=(z[i+1]-z[i])/(6*h[i])
    f[i]=(z[i]/2)
    g[i]=b[i]-h[i]*((z[i+1]+2*z[i])/6)
    o[i]=y[i]

o[n-1]=y[n-1]
g[n-1]=3*e[n-2]*(h[n-2]**2)+2*f[n-2]*(h[n-2])+g[n-2]
f[n-1]=z[n-1]/2
e[n-1]=((y[n]-y[n-1])-(f[n-1]*(h[n-1]**2)+g[n-1]*h[n-1]))/(h[n-1]**3)

print("Coefficients e[i] :",e)
print("Coefficients f[i] :",f)
print("Coefficients g[i] :",g)
print("Coefficients o[i] :",o)

#===


# Construct the spline polynomials
n = len(x)-1

t = []
u = []
axis = []

for i in range(0,n):
    t = np.linspace(x[i],x[i+1],num=100)
    axis = np.append(axis,t)
    func = e[i]*((t-x[i])**3)+f[i]*((t-x[i])**2)+g[i]*(t-x[i])+o[i]
    u = np.append(u,e[i]*((t-x[i])**3)+f[i]*((t-x[i])**2)+g[i]*(t-x[i])+o[i])

plt.plot(axis, u, 'b',x,y,'ro')
for i in range(0,n+1):
    s = "("+str(x[i])+","+str(y[i])+")"
    plt.annotate(s,xy=(x[i],y[i]),xytext=(x[i]+0.25,y[i]+1),)
plt.grid(True)
print(func)
plt.show()