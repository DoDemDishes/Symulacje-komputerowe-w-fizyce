import numpy as np

n = 7
v = np.zeros(n)

for i in range(n):
    v[i] = i/2.0
print "v = ", v

u = np.arange(-1.,1.,0.2)
print "u = ", u

w = np.linspace(-np.pi, np.pi,6)
print "w = ", w
