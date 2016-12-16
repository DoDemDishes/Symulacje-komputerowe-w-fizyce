import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Circle

miss = 0
particles = []
particles_temp = []
i = 0
boxsize = 300
n = 1
k = 1
r = 5
class czastka:
	def __init__(self, position, agr):
		self.pos = position
		self.agregat = agr

def ruch (particle):
    random = np.random.randint(0,4)
    if random == 0:
        particle.pos = particle.pos + np.array([1,0])
    if random == 1:
        particle.pos = particle.pos + np.array([-1,0])
    if random == 2:
        particle.pos = particle.pos + np.array([0,1])
    if random == 3:
        particle.pos = particle.pos + np.array([0,-1])
    return particle.pos

def position(R):
    rad = np.random.uniform(0,2*np.pi)
    r = np.array([int(R*math.cos(rad)), int(R*math.sin(rad))])
    return r

def sprawdz_okolice(czastka,particles):
    test = False
    for i in particles:
        if np.linalg.norm(czastka.pos - i.pos) == 1:
            test = True
    return test

def czy_zabic(czastka,r):
	if np.linalg.norm(czastka.pos) > (r + 150):
		return True
	else:
		return False

particles.append(czastka(np.array([0,0]), True))
while len(particles) < 5000:
    if len(particles)%(n*10) == 0:
        print 'trafione: ', len(particles), ' chybione: ', miss
        n += 1
    ##wygeneruj czastke
    particles_temp.append(czastka(position(r+2),False))
    while particles_temp[i].agregat == False:
        ##wykonaj ruch
        particles_temp[i].pos = ruch(particles_temp[i])
        ##sprawdz okolice
        particles_temp[i].agregat = sprawdz_okolice(particles_temp[i], particles)
        if particles_temp[i].agregat == True:
            particles.append(particles_temp[i])
            if np.linalg.norm(particles_temp[i].pos) > r:
                r = np.linalg.norm(particles_temp[i].pos)
        ##sprawdz promien
        if czy_zabic(particles_temp[i],r) == True:
			miss += 1
			break
    ##rysuj
    if (len(particles)%(k*25) == 0):
        k += 1
        plt.clf()
        F = plt.gcf()
        for i in range(len(particles)):
            p = particles[i]
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
    i += 1
