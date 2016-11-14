import numpy as np
import matplotlib.pyplot as py
from matplotlib.patches import Circle

Nparticles = 16
boxsize = 8.
sigma = 1.
r = 0.5
dt = 0.0001
delta = 1.3
kT = 0.1
temp = kT
TMAX = 3

def getDistanceVect(p1, p2):
    rv = p2.x-p1.x
    b2 = boxsize/2
    if rv[0] > b2:
        rv[0] = rv[0] - boxsize
    elif rv[0] < -b2:
        rv[0] = rv[0]+boxsize

    if rv[1] > b2:
        rv[1] = rv[1]-boxsize
    elif rv[1] < -b2:
        rv[1] = rv[1]+boxsize
    return rv

def force(p1, p2):
    rr = getDistanceVect(p1, p2)
    mod = np.linalg.norm(rr)
    if mod > 2.5*sigma:
        return 0;
    ff = 48/sigma *((sigma/mod)**14 - 1./2 * (sigma/mod)**8)
    return -ff*(rr)

def Vpot(p1, p2):
    rr = getDistanceVect(p1, p2)
    mod = np.linalg.norm(rr)
    if mod > 2.5*sigma:
        return 0;
    ff = 4*((sigma/mod)**12 - (sigma/mod)**6)
    return ff

class particle:
    def __init__(self, x, v, r=r):
        self.x = x
        self.v = v
        self.r = r

particles = []

# Init
V0 = np.random.uniform(size=2*Nparticles)
V0.shape = [Nparticles, 2]
vmean = V0.mean(axis=0)
V0 = V0 - vmean
meanEv = np.mean(np.array(list(map(lambda i: np.dot(V0[i], V0[i]), range(V0.shape[0])))))
fs = np.sqrt(kT/meanEv)
V0 = V0*fs
#print(V0)

nsqrt = int(np.sqrt(Nparticles))
for i in range(nsqrt):
    for j in range(nsqrt):
        x0 = np.array([i*delta, j*delta])
        particles.append(particle(x0, V0[i*nsqrt+j]))

Ek = np.zeros(int(TMAX/dt))
Ep = np.zeros(int(TMAX/dt))

for i in range(int(TMAX/dt)):
#    for j in range(Nparticles):
#        p = particles[j]
#        p.x += p.v*dt
#        p.x %= boxsizei
    import copy
    particles_temp = copy.deepcopy(particles)
    for j in range(Nparticles):
        for k in range(Nparticles):
            if k != j:
                p1 = particles_temp[j]
                p2 = particles_temp[k]
                p1.v = p1.v + force(p1, p2)*dt/2
    Tt = 1./Nparticles * sum(map(lambda p: np.dot(p.v, p.v), particles_temp))
    Ek[i] = Tt
    eta = np.sqrt(temp/Tt)
    # if (i%100 ==.0):
    # print("Tt: {}, eta: {}".format(Tt, eta))

    V_temp = 0
    for j in range(Nparticles):
        f_temp = 0
        p1 = particles[j]

        for k in range(Nparticles):
            if k != j:
                p2 = particles[k]
                f_temp += force(p1, p2)
                V_temp += Vpot(p1, p2)
        p1.v = (2*eta-1)*p1.v + eta*f_temp*dt
    Ep[i] = V_temp


    for j in range(Nparticles):
        p1 = particles[j]
        p1.x = p1.x + p1.v*dt
        p1.x %= boxsize

    if (i%100==0):
        print("{}/{}".format(i, TMAX/dt))
        py.clf()
        F = py.gcf()
        for j in range(Nparticles):
            p = particles[j]
            a = py.gca()
            cir = Circle((p.x[0], p.x[1]), radius=p.r)
            a.add_patch(cir)
            py.plot()
        py.xlim((0, boxsize))
        py.ylim((0, boxsize))
        F.set_size_inches((6,6))
        py.title("Symulacja gazu Lennarda-Jonesa, krok {:0=5d}".format(i))
        py.savefig('plots/img_{:0=5d}.png'.format(i))

py.figure()
py.plot(Ep)
py.plot(Ek)
py.savefig("energy.png")
