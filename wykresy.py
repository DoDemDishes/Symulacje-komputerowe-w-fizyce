import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 111)

y1 = np.cos(x)
y2 = np.sin(x)

#plt.plot(x, y1, color = 'r', linestyle = '-', linewidth = 2)
#plt.plot(x, y2, 'ro', lw = 2)
plt.plot(x, x, 'r--', x, x**2, 'bs',\
                            x, x**3, 'g^')


plt.xlabel('x dana', fontsize = 20)
plt.ylabel('y dana', fontsize = 20)
plt.title('Funkcje: sinus i cosinus', fontsize = 24)

plt.grid(True)
plt.legend(('cos(x)','sin(x)'))
plt.show()
