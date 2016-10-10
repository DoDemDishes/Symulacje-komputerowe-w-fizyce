import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#1A i 1B
lista = np.random.normal(10.,1.5,10000)
lista.sort()
mu = np.average(lista)
sigma = np.std(lista)
s =  "Srednia %6.2f odchylenie %6.2f" % (mu,sigma)
print s

#1C
n = 1000
xprob = np.zeros(n)
for i in xrange(10):
    xprob += np.random.uniform(-1.,1.,n)
xnew = mu + sigma * xprob * np.sqrt(3./10)

print xnew

#Rysowanie wykresow
plt.figure(1)
plt.subplot(211)
plt.hist(lista, bins = 20, normed = True)
plt.plot(lista, mlab.normpdf(lista,mu,sigma))
plt.title(s)
plt.subplot(212)
plt.hist(xnew, bins = 20, normed = True)
plt.show()
