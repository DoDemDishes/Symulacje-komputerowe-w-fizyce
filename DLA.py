import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Circle

particles_temp = []
particles = []
R = 1
en = 1
boxsize = 100.0


class czastka:
	def __init__(self, position, agr = False):
		self.pos = position
		self.agregat = agr

def ruch(czastka):
	random = np.random.randint(1,5)
	if random == 1:
		czastka.pos = czastka.pos + np.array([1,0])
	if random == 2:
		czastka.pos = czastka.pos + np.array([0,1])
	if random == 3:
		czastka.pos = czastka.pos + np.array([-1,0])
	if random == 4:
		czastka.pos = czastka.pos + np.array([0,-1])
	print 'jestem w funkcji ruch'
	return czastka.pos

def generuj_polozenie(R):
	random = np.random.randint(0,360)
	rad = math.radians(random)
	r = [int(R*math.cos(rad)), int(R*math.sin(rad))]
	print 'jestem w funkcji generuj_polozenie'
	return r


def r_max(particles):
	r = []
	for i in particles:
		r.append(np.linalg.norm(i.pos))
	rmax = max(r)
	print 'jestem w funkcji r_max'
	return rmax

def generuj_czastke(particles_temp,R):
	r = generuj_polozenie(R+5)
	particles_temp.append(czastka(r))
	print 'jestem w funkcji generuj_czastke'

def czy_zabic(czastka,R):
	zabic = False
	if np.linalg.norm(czastka.pos) > R*2:
		zabic = True
	print 'jestem w funkcji czy_zabic'
	return zabic

def sprawdz_okolice(particles,czastka):
	for i in particles:
		if np.linalg.norm(i.pos - czastka.pos) < 1:
			return True
		else:
			return False
	print 'jestem w funkcji sprawdz_okolice'
### Inicjalizacja

temp = np.array([0,0])
particles.append(czastka(temp, True))
particles_temp.append(czastka(temp, True))

for i in xrange(1000):
	print i
	R = r_max(particles)
	generuj_czastke(particles_temp,R)
	while particles_temp[i+1].agregat == False:
		# print particles_temp[i+1].pos, 'R ', R, 'Dlugosc ', np.linalg.norm(particles_temp[i+1].pos)
		ruch(particles_temp[i+1])
		particles_temp[i+1].agregat = sprawdz_okolice(particles,particles_temp[i+1])
		if czy_zabic(particles_temp[i+1], R) == True:
			break
		if particles_temp[i+1].agregat == True:
			particles.append(particles_temp[i+1])
	if (en%1 == 0):
		plt.clf()
		F = plt.gcf()
		for i in range(len(particles_temp)):
			p = particles_temp[i]
			a = plt.gca()
			cir = Circle((p.pos), 0.4, color = 'black')
			a.add_patch(cir)
			plt.plot()
		plt.xlim((-boxsize, boxsize))
		plt.ylim((-boxsize ,boxsize))
		F.set_size_inches((6,6))
		nStr = str(en)
		nStr = nStr.rjust(5,'0')
		plt.title('krok' + nStr)
		plt.savefig('dla/img' + nStr + '.png')
	en += 1
