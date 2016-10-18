import matplotlib.pyplot as plt
import numpy as np

G = 0.01
dt = 0.001
liczba_iteracji = 10000

class planeta:
    """ Klasa opisujaca pojedyncza """
    def __init__(self,radius,mass,pos,vel):
        self.rad = radius
        self.m = mass
        self.r = pos # polozenie
        self.v = vel # predkosc

class gwiazda:
    """ Klasa opisujaca pojedyncza """
    def __init__(self,radius,mass,pos,vel):
        self.rad = radius
        self.m = mass
        self.r = pos # polozenie
        self.v = vel # predkosc

def force (radius, mass1, mass2):
    f = -(G*mass1*mass2)/(np.linalg.norm(radius)**2) * (radius/np.linalg.norm(radius))
    return f

def potential (radius, mass1, mass2):
    p = -G*mass1*mass2/(np.linalg.norm(radius))
    return p

def verlet_start (r0, v0):
    start = r0 - v0*dt
    polozenia.append(start)
    polozenia.append(r0)

def kinetic (planeta, v):
    kin = (1/2) * planeta.m * (v**2)

def euler_start (tablica_polozen, tablica_pedow, r0, v0, mass):
    tablica_polozen.append(r0)
    tablica_pedow.append(v0 * mass)

def leapfrog_start (planeta, tabela_predkosci, tabela_polozen, gwiazda):
    vminus = planeta.v - (1/planeta.m)*(force(planeta.r, planeta.m, gwiazda.m)/(planeta.m))*(1/2)*dt
    tabela_predkosci.append(vminus)
    tabela_polozen.append(planeta.r)

def verlet (tablica, liczba_iteracji, planeta, gwiazda, tablica_kinetyczna):
    for i in xrange(liczba_iteracji):
        rn = 2*tablica[i+1] - tablica[i] + force(tablica[i+1], planeta.m, gwiazda.m)/(planeta.m)*(dt**2)
        tablica.append(rn)
        p = potential(rn, planeta.m, gwiazda.m)
        potencjaly.append(p)
        v = (tablica[i+1]-tablica[i])/(2*dt)
        tablica_kinetyczna.append(kinetic(andrzej7000, v))

def euler (tablica_polozen, tablica_pedow, liczba_iteracji, planeta, gwiazda):
    for i in xrange(liczba_iteracji):
        rn = tablica_polozen[i] + tablica_pedow[i]*dt/planeta.m + (1/2)*force(tablica_polozen[i], planeta.m, gwiazda.m)/(planeta.m)*(dt**2)
        pn = tablica_pedow[i] + force(tablica_polozen[i], planeta.m, gwiazda.m)*dt
        tablica_polozen.append(rn)
        tablica_pedow.append(pn)

def leapfrog(liczba_iteracji, tabela_predkosci, tabela_polozen, planeta, gwiazda):
    for i in xrange(liczba_iteracji):
        vn = tabela_predkosci[i] + (force(tabela_polozen[i], planeta.m, gwiazda.m)/planeta.m)*(dt**2)
        rn = tabela_polozen[i] + vn*dt
        tabela_predkosci.append(vn)
        tabela_polozen.append(rn)

def rysuj_orbite (liczba_iteracji, polozenia, planeta, gwiazda):
    fig, ax = plt.subplots(figsize=(8,8))
    star = plt.Circle((gwiazda.r), gwiazda.rad, color = 'blue')
    ax.add_artist(star)
    for i in xrange(liczba_iteracji):
        planet = plt.Circle((polozenia[i]), planeta.rad, color = 'g')
        ax.add_artist(planet)
    fig.savefig('orbita.png')
    plt.xlim(-1,4)
    plt.ylim(-2,2)
    plt.show()

def rysuj_potencjal (potencjaly, liczba_iteracji):
        plt.plot(xrange(liczba_iteracji),potencjaly)
        plt.show()

czomberbomber123 = gwiazda(0.1, 500., np.array([0.,0.]), np.array([0.,0.]))
andrzej7000 = planeta(0.01, 0.1, np.array([2., 0.]), np.array([0., 1.]))

polozenia = [] #lista kolejnych polozen planety
potencjaly = [] #lista energii potencjalnej w kazdym punkcie
pedy = [] #lista pedow w kazdym punkcie
predkosci = [] #list predkosci w kazdym punkcie
kinetyczna = []
# Verlet
verlet_start(andrzej7000.r, andrzej7000.v)
verlet(polozenia, liczba_iteracji, andrzej7000, czomberbomber123, kinetyczna)
# #rysuj_orbite(liczba_iteracji, polozenia, andrzej7000, czomberbomber123)
# rysuj_potencjal(potencjaly, liczba_iteracji)
###################

# Euler
# euler_start(polozenia, pedy, andrzej7000.r, andrzej7000.v, andrzej7000.m)
# euler(polozenia, pedy, liczba_iteracji, andrzej7000, czomberbomber123)
# rysuj_orbite(liczba_iteracji, polozenia, andrzej7000, czomberbomber123)
##################

# Leapfrog
# leapfrog_start(andrzej7000, predkosci, polozenia, czomberbomber123)
# leapfrog(liczba_iteracji, predkosci, polozenia, andrzej7000, czomberbomber123)
# rysuj_orbite(liczba_iteracji, polozenia, andrzej7000, czomberbomber123)
#################


fig, ax = plt.subplots(figsize=(8,8))
plt.figure(1)
plt.subplot(211)
star = plt.Circle((czomberbomber123.r), czomberbomber123.rad, color = 'blue')
ax.add_artist(star)
for i in xrange(liczba_iteracji):
    planet = plt.Circle((polozenia[i]), andrzej7000.rad, color = 'g')
    ax.add_artist(planet)
plt.subplot(212)
plt.plot(xrange(liczba_iteracji),potencjaly)
# plt.subplot(213)
# plt.plot(xrange(liczba_iteracji),kinetyczna)
# plt.subplot(214)
# plt.plot(xrange(liczba_iteracji),kinetyczna+potencjaly)
fig.savefig('orbita.png')
plt.xlim(-1,4)
plt.ylim(-2,2)
plt.show()
