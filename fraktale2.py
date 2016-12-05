import numpy as np
from numpy import array, zeros
from numpy.random import randint, random
import matplotlib.pyplot as plt


### Stale
nr = input("Co sprawdzamy? \n 0 - Trojkaty Sierpinskiego \n 1 - Paprotki Barnsley'a \n")
liczba_iteracji = 100000
liczba_podzialow = 8

def create_table(nr,liczba_iteracji):
	p = None
	tmp = None
	for i in xrange(100000):
		if nr == 0:
			p = randint(0,3)
		if nr == 1:
			tmp = random()
			if tmp < 0.73: 	p = 0
			elif tmp < 0.86: p = 1
			elif tmp < 0.97: p = 2
			else: p = 3
		tab[p] += 1
		xpoints.append(m[nr][p,0]*xpoints[-1] + m[nr][p,1]*ypoints[-1] + m[nr][p,4])
		ypoints.append(m[nr][p,2]*xpoints[-2] + m[nr][p,3]*ypoints[-1] + m[nr][p,5])

def siatka():
	stosunek = []
	tab_N = []
	for N in xrange(1,liczba_podzialow+1):
		pole = zeros([2**N,2**N])
		ax = np.floor( (xpoints - x_min) / (x_max - x_min + 0.0001) * 2**N)
		ay = np.floor( (ypoints - y_min) / (y_max - y_min + 0.0001) * 2**N)
		for k in xrange(len(xpoints)):
			pole[ax[k], ay[k]] = 1
		stosunek.append(np.sum(pole))
		tab_N.append(2**N)
	return [tab_N,stosunek]
m = [0]*2
#p = 0
# trojkat Sierpinskiego
m[0] = array([[0.5,0.,0.,0.5,0.,0.],[0.5,0.,0.,0.5,0.5,0.],[0.5,0.,0.,0.5,0.25,np.sqrt(3./4)]])
# paprotka
m[1] = array([[0.85,0.04,-0.04,0.85,0.,1.6],[0.2,-0.26,0.23,0.22,0.,1.6],[-0.15,0.28,0.26,0.24,0.,0.44],[0.,0.,0.,0.16,0.,0.]])

tab = [0]*4

xpoints = [0.]
ypoints = [0.]

create_table(nr, liczba_iteracji)
#print np.array(tab)/float(liczba_iteracji)

ax = plt.gca()
ax.set_axis_bgcolor('black')
plt.figure(1)
plt.scatter(xpoints, ypoints, s=1, marker=".", lw=0, c='y')
#plt.show()
#plt.savefig('paprotka.png')

x_min = min(xpoints)
x_max = max(xpoints)
y_min = min(ypoints)
y_max = max(ypoints)

xpoints = array(xpoints)
ypoints = array(ypoints)

siatka = siatka()

# print siatka[0]
# print siatka[1]

iksy = np.log(np.array(siatka[0]))
igreki = np.log(np.array(siatka[1]))

# print iksy
# print igreki

plt.figure(2)
#plt.scatter(siatka[0], siatka[1], s=1, marker=".", lw=0, c='y')
plt.scatter(iksy,igreki,marker="o")
# plt.show()
plt.savefig('trojkaty.png')

coeff = np.polyfit(iksy,igreki,deg=1)
print coeff
