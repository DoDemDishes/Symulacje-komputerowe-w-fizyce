import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Parametry
N = 100
D_u = 2*10**(-5)
D_v = 1*10**(-5)
F = 0.032
k = 0.056
dx = 0.02
dt = 1
en = 1
t_max = 32000
odcinek = np.linspace(0,2,N)

u = np.ones((N,N))
v = np.zeros((N,N))
for i in range(N/4, 3*N/4):
    for j in range(N/4, 3*N/4):
        u[i][j] = np.random.uniform(0.4,0.6)
        v[i][j] = np.random.uniform(0.2,0.4)

while en <= t_max:
    u_new = (D_u * (np.roll(u,1,axis=0) + np.roll(u,-1,axis=0) + np.roll(u,1,axis=1) + np.roll(u,-1,axis=1) - 4*u)/dx**2 - u*v*v + F*(1-u))*dt
    v_new = (D_v * (np.roll(v,1,axis=0) + np.roll(v,-1,axis=0) + np.roll(v,1,axis=1) + np.roll(v,-1,axis=1) - 4*v)/dx**2 + u*v*v - (F+k)*v)*dt
    u += u_new
    v += v_new
    en += 1
    if en%25==0:
        plt.clf()
        fig=plt.figure()
        ax=fig.add_subplot(111)
        nStr=str(en)
        nStr = nStr.rjust(5,'0')
        cax = ax.imshow(v, interpolation='nearest')
        cax.set_clim(vmin=0, vmax=1)
        cbar = fig.colorbar(cax, ticks=[0,0.3, 0.5,1], orientation='vertical')
        plt.title("k = "+str(k)+"; F = "+str(F))
        plt.savefig('reakcja2/img '+nStr+'.png')
