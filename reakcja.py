import numpy as np
import matplotlib.pyplot as plt

#Parametry
N = 100
D_u = 2*10**(-5)
D_v = 1*10**(-5)
F = 0.025
k = 0.055

odcinek = np.linspace(0,2,N)

u = np.ones(N)
v = np.zeroes(N)
xs = np.arange(N)

for i in range(N/4,3*N/4):
    u[i] = random()*0.2 + 0.4
    v[i] = random()*0.2 + 0.2
