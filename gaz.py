import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class czastka:
	def __init__ (self,promien,pos,vel):
		self.promien = promien
		self.r = pos
		self.v = vel

particleNumber = 16
boxsize = 8.0
eps = 1.0
sigma = 1.0
promien = 0.02
deltat = 0.0001
kT = 2.5
delta = 0.2


particles = []

for i in range(4):
	for j in range(4):
		polozenie = np.array([i*delta, j*delta])
		predkosc = np.array([(np.random.random()-1./2),(np.random.random()-1./2)])
		particles.append(czastka(promien,polozenie,predkosc))

for i in particles:
	print i.r
en = 0
if (en%100 == 0):
	plt.clf()
	F = plt.gcf()
	for i in range(particleNumber):
		p = particles[i]
		radius = p.promien
		a = plt.gca()
		cir = Circle((p.r[0], p.r[1], radius))
		a.add_patch(cir)
		plt.plot()
	en += 1
plt.xlim((0,boxsize))
plt.ylim((0,boxsize))
F.set_size_inches((6,6))
nStr = str(en)
nStr = nStr.rjust(5,'0')
plt.title('Symulacja gazu Lennarda-Jonesa, krok' + nStr)
plt.savefig('img' + nStr + '.png')
plt.show()
