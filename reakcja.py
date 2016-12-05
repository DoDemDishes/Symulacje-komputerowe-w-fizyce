import numpy as np
import matplotlib.pyplot as plt

#Parametry
N = 100
D_u = 2*10**(-5)
D_v = 1*10**(-5)
F = 0.025
k = 0.055
dx = 0.2
dt = 1
en = 1

odcinek = np.linspace(0,2,N)

u = np.ones(N)
v = np.zeros(N)
xs = np.arange(N)

for i in range(N/4,3*N/4):
    u[i] = np.random.random()*0.2 + 0.4
    v[i] = np.random.random()*0.2 + 0.2

while 1:
    u_new = (D_u * (((np.roll(u,1) - np.roll(u,-1)-2*u))/dx**2) - u*v**2 + F*(1-u))*dt
    v_new = (D_v * (((np.roll(v,1) - np.roll(v,-1)-2*u))/dx**2) + u*v**2 - v*(F+k))*dt
    u += u_new
    v += v_new
    # print u_new
    # print v_new
    plt.scatter(xs,v)
    plt.savefig('reakcja/img' + str(en) + '.png')
    plt.clf()
    en += 1
