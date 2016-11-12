import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class czastka:
	def __init__(self,pos,vel,promien = 0.5):
		self.promien = promien
		self.r = pos # polozenie
		self.r_old = None
		self.v = vel # predkosc
		self.v_half = None
	def PBC(self):
		if self.r[0] > boxsize:
			self.r[0] -= boxsize
		if self.r[0] < 0:
			self.r[0] += boxsize
		if self.r[1] > boxsize:
			self.r[1] -= boxsize
		if self.r[1] < 0:
			self.r[1] += boxsize

# PARAMETRY POCZATKOWE

particleNumber = 16
boxsize = 8.
eps = 1.0
sigma = 1.0
deltat = 0.0001
kT = 0.1
masa = 1.
delta = np.sqrt(particleNumber)
t_max = 30

# TWORZENIE CZASTECZEK

particles = []
for i in xrange(int(delta)):
	for j in xrange(int(delta)):
		polozenie = np.array([i*delta/2, j*delta/2])
		predkosc = np.array([(np.random.random()-1./2),(np.random.random() -1./2)])
		particles.append(czastka(polozenie,predkosc) )
sumv = 0.0
sumv2 = 0.0
for p in particles:
	sumv = sumv+p.v
sumv = sumv/particleNumber # predkosc srodka masy

for p in particles:
	p.v = (p.v-sumv) # teraz srodek masy spoczywa
for p in particles:
	sumv2 = sumv2+np.dot(p.v,p.v)/2.0
sumv2 = sumv2/particleNumber # srednia energia kinetyczna
fs = np.sqrt(kT/sumv2) # czynnik skalujacy, kT - zadana temperatura
for p in particles:
	p.v = p.v*fs

def najb_obraz(cz1, cz2):
	r_vect = cz2.r - cz1.r # wektor pomiedzy czastkami i oraz j
	if r_vect[0] > boxsize/2: # b2 polowa pudelka
		r_vect[0] = r_vect[0] - boxsize # przesuwamy wspolrzedna x wektora r_vect
	elif r_vect[0] < -boxsize/2:
		r_vect[0] = r_vect[0] + boxsize # b bok pudelka

	if r_vect[1] > boxsize/2: # to samo dla y
		r_vect[1] = r_vect[1] - boxsize
	elif r_vect[1] < -boxsize/2:
		r_vect[1] = r_vect[1] + boxsize
	return r_vect

def sila(cz1,cz2):
	r = najb_obraz(cz1, cz2)
	r_norm = np.linalg.norm(r)
	if r_norm == 0:
		return np.array([0,0])
	elif r_norm < 2.5:
		Fx = -48*eps/sigma * ((sigma/r_norm )**14 - (1./2)*(sigma/r_norm )**8)*r[0]
		Fy = -48*eps/sigma * ((sigma/r_norm )**14 - (1./2)*(sigma/r_norm )**8)*r[1]
		return np.array([Fx,Fy])
	else:
		return np.array([0,0])

def uzupelnij(cz1, new_r, new_v, v_half_2):
	cz1.r_old = cz1.r
	cz1.r = new_r
	cz1.v_half = v_half_2
	cz1.v = new_v	

#F = [0.]*particleNumber
T = []

class Krok(object):
	def __init__(self):
		self.en = 0 # numer kroku
		self.F = [0.]*particleNumber
	def wykonaj_krok(self):
									# Obliczam sily
		for i in range(len(particles)):
			for particle in particles:
				self.F[i] += sila(particles[i],particle)
									# Obliczam polozenia i predkosci
		if self.en == 0:
			for i in range(len(particles)):
				algorytm_leapfrog(particles[i],i,start = 'tak')
				particles[i].PBC()
		else:
			for i in range(len(particles)):
				algorytm_leapfrog(particles[i],i)
				particles[i].PBC()
		v_2 = 0						# Obliczam energie kinetyczna
		for i in range(len(particles)):
			v_2 += np.dot(particles[i].v,particles[i].v)

		T.append(v_2*masa/(2*particleNumber))


def algorytm_leapfrog(cz1,i,**start):
	if start.get("start") == 'tak':
		v_half_1 = cz1.v - krok.F[i]*deltat/(2*masa)
	else:
		v_half_1 = cz1.v_half
	v_half_2 = v_half_1 + krok.F[i]*deltat/masa
	new_r = cz1.r + v_half_2*deltat
	new_v = (v_half_1+v_half_2)/2
	uzupelnij(cz1, new_r, new_v, v_half_2)

t = 0

krok = Krok()

while t < t_max+deltat:

	krok.wykonaj_krok()

	t += deltat

	if ((krok.en-1)%300==0): # co 1000-na klatka
		plt.clf() # wyczysc obrazek
		Fig = plt.gcf() # zdefiniuj nowy
		for i in range(particleNumber): # petla po czastkach
			p = particles[i]
			a = plt.gca() # get current axes (to add smth to them)
			cir = Circle((p.r[0],p.r[1]), radius=p.promien) # kolko tam gdzie jest czastka
			a.add_patch(cir) # dodaj to kolko do rysunku
			plt.plot() # narysuj
		plt.xlim((0,boxsize)) # obszar do narysowania
		plt.ylim((0,boxsize))
		Fig.set_size_inches((6,6)) # rozmiar rysunku
		nStr=str(krok.en-1) #nagraj na dysk numer pliku z 5 cyframi, na poczatku zera, np 00324.png
		nStr=nStr.rjust(5,'0')
		plt.title("Symulacja gazu Lennarda-Jonesa, krok "+nStr)
		plt.savefig('img'+nStr+'.png')
	krok.en += 1
	krok.F = [0.]*particleNumber


#print T
fig, ax = plt.subplots() 

plt.figure(2)
plt.plot(xrange(krok.en), T, color='r', linestyle='-', linewidth=2)
plt.savefig('_Temp.png')





















