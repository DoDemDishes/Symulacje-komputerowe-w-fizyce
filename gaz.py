import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

particleNumber = 16
particleMass = 0.05
boxsize = 8.0
eps = 1.0
sigma = 1.0
radius = 0.4
deltat = 0.001
kT = 2.5
delta = 2
tmax = 10
t = 0
en = 0

class czastka:
	def __init__ (self,radius,pos,vel,force, mass):
		self.radius = radius
		self.r = pos
		self.v = vel
		self.f = force
		self.m = mass

def force (particle, particles):
	force = np.array([0,0])
	for i in particles:
		if i == particle:
			continue
		temp = -(48.*eps)/(sigma**2)*((sigma/(np.linalg.norm(i.r - particle.r))))**14-\
		(1./2.)*(sigma/(np.linalg.norm(i.r - particle.r))**8)*\
		np.array([(i.r[0]-particle.r[0]),(i.r[1]-particle.r[1])])
		force = np.add(force, temp)
	return force

particles = []



for i in range(4):
	for j in range(4):
		position = np.array([i*delta, j*delta])
		velocity = np.array([(np.random.random()-1./2),(np.random.random()-1./2)])
		particles.append(czastka(radius,position,velocity,0,particleMass))

while t < tmax:
	for i in xrange(particleNumber):
		particles[i].f = force(particles[i],particles)
	for j in xrange(particleNumber):
		particles[j].v = particles[j].v + (particles[j].f/particles[j].m) * deltat
		particles[j].r = particles[j].r + particles[j].v * deltat

	if (en%100 == 0):
		plt.clf()
		F = plt.gcf()
		for i in range(particleNumber):
			p = particles[i]
			a = plt.gca()
			cir = Circle((p.r), p.radius, color = 'g')
			a.add_patch(cir)
			plt.plot()
		plt.xlim((-1,boxsize))
		plt.ylim((-1,boxsize))
		F.set_size_inches((6,6))
		nStr = str(en)
		nStr = nStr.rjust(5,'0')
		plt.title('Symulacja gazu Lennarda-Jonesa, krok' + nStr)
		plt.savefig('gazy/img' + nStr + '.png')
	en += 1
	t += deltat
