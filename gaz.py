import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

particleNumber = 16
particleMass = 0.1
boxsize = 8.0
eps = 0.05
sigma = 0.8
radius = 0.3
deltat = 0.001
kT = 2.5
delta = 1.5
tmax = 10
t = 0
en = 0
plt.ion()

class czastka:
	def __init__ (self,radius,pos,vel,force, mass):
		self.radius = radius
		self.r = pos
		self.v = vel
		self.f = force
		self.m = mass

def force (particle, particles):
	force_array = np.array([0,0])
	for i in particles:
		if i == particle:
			continue
		if np.array_equal(i.r, particle.r):
			continue
		### Nie mam pojecia co to robi :X
		r_vect = i.r-particle.r
		if r_vect[0] > boxsize/2.:
			r_vect[0] = r_vect[0] - boxsize
		elif r_vect[0] < -boxsize/2.:
			r_vect[0] = r_vect[0] + boxsize

		if r_vect[1] > boxsize/2.:
			r_vect[1] =r_vect[1] - boxsize
		elif r_vect[1] < -boxsize/2.:
			r_vect[1] =r_vect[1] + boxsize

		r = np.linalg.norm(r_vect)
		rx = np.array(r_vect[0])
		ry = np.array(r_vect[1])
		force = -(48.*eps)/(sigma)*((sigma/r)**14 - 1./2.*(sigma/r)**8)*np.array([rx,ry])
		force_array = np.add(force_array, force)
	# print np.linalg.norm(force_array)
	return force_array

#### Kreacja czastek
particles = []

for i in range(4):
	for j in range(4):
		position = np.array([(i+1)*delta, (j+1)*delta])
		velocity = np.array([(np.random.random()-1./2),(np.random.random()-1./2)])
		particles.append(czastka(radius,position,velocity,0,particleMass))

#### Inicjalizacja predkosci
for i in particles:
	i.v = i.v - 1/i.m * force(i,particles) * 1./2. * deltat

#### Glowna petla programu
while t < tmax:
	kinetic_energy = 0
	potential_energy = 0
	for i in xrange(particleNumber):
		particles[i].f = force(particles[i],particles)
		particles[i].v = particles[i].v + (particles[i].f/particles[i].m) * deltat
		particles[i].r = (particles[i].r + particles[i].v * deltat)
		#### Najblizszy obraz
		if particles[i].r[0] > boxsize:
			particles[i].r[0] -= boxsize
		if particles[i].r[0] < 0:
			particles[i].r[0] += boxsize
		if particles[i].r[1] > boxsize:
			particles[i].r[1] -= boxsize
		if particles[i].r[1] < 0:
			particles[i].r[1] += boxsize

		kinetic_energy += 1./2 * particles[i].m * np.linalg.norm(particles[i].v)**2

	if (en%100 == 0):
		# print kinetic_energy
		plt.clf()
		F = plt.gcf()
		for i in range(particleNumber):
			c = plt.cm.cool(np.linalg.norm(particles[i].v))
			p = particles[i]
			a = plt.gca()
			cir = Circle((p.r), p.radius, color = c)
			a.add_patch(cir)
			plt.plot()
		plt.xlim((0, boxsize))
		plt.ylim((0 ,boxsize))
		F.set_size_inches((6,6))
		nStr = str(en)
		nStr = nStr.rjust(5,'0')
		plt.title('Symulacja gazu Lennarda-Jonesa, krok' + nStr)
		# plt.savefig('gazy/img' + nStr + '.png')
		plt.pause(0.000001)
		print kinetic_energy
	en += 1
	t += deltat
