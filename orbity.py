import matplotlib.pyplot as plt
import numpy as np
from operator import add

G = 0.01
dt = 0.001
liczba_iteracji = 5000

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

def kinetic (planeta, v):
    kin = (1./2.)*planeta.m*(v**2)
    return kin

def verlet_start (r0, v0):
    start = r0 - v0*dt
    polozenia.append(start)
    polozenia.append(r0)

def euler_start (lista_polozen, lista_pedow, r0, v0, mass):
    lista_polozen.append(r0)
    lista_pedow.append(v0 * mass)

def leapfrog_start (planeta, lista_predkosci, lista_polozen, gwiazda):
    vminus = planeta.v - (force(planeta.r, planeta.m, gwiazda.m)/planeta.m)*(dt/2)
    lista_predkosci.append(vminus)
    lista_polozen.append(planeta.r)

def verlet (lista_polozen, liczba_iteracji, planeta, gwiazda, lista_kinetyczna, lista_potencjalow):
    for i in xrange(liczba_iteracji):
        rn = 2*lista_polozen[i+1] - lista_polozen[i] + (force(lista_polozen[i+1], planeta.m, gwiazda.m)/(planeta.m))*(dt**2)
        lista_polozen.append(rn)
        p = potential(rn, planeta.m, gwiazda.m)
        lista_potencjalow.append(p)
        v = (lista_polozen[i+1]-lista_polozen[i-1])/(2*dt)
        lista_kinetyczna.append(kinetic(planeta, np.linalg.norm(v)))

def euler (lista_polozen, lista_pedow, liczba_iteracji, planeta, gwiazda, lista_kinetyczna, lista_potencjalow):
    for i in xrange(liczba_iteracji):
        rn = lista_polozen[i] + lista_pedow[i]*dt/planeta.m + (1/2)*force(lista_polozen[i], planeta.m, gwiazda.m)/(planeta.m)*(dt**2)
        pn = lista_pedow[i] + force(lista_polozen[i], planeta.m, gwiazda.m)*dt
        lista_polozen.append(rn)
        lista_pedow.append(pn)
        p = potential(rn, planeta.m, gwiazda.m)
        potencjaly.append(p)
        v = pn/planeta.m
        lista_kinetyczna.append(kinetic(planeta, np.linalg.norm(v)))

def leapfrog(liczba_iteracji, lista_predkosci, lista_polozen, planeta, gwiazda, lista_kinetyczna, lista_potencjalow):
    for i in xrange(liczba_iteracji):
        vn = lista_predkosci[i] + (force(lista_polozen[i], planeta.m, gwiazda.m)/planeta.m)*dt
        rn = lista_polozen[i] + vn*dt
        lista_predkosci.append(vn)
        lista_polozen.append(rn)
        p = potential(rn, planeta.m, gwiazda.m)
        potencjaly.append(p)
        lista_kinetyczna.append(kinetic(planeta, np.linalg.norm(vn)))

def rysuj_orbite (liczba_iteracji, polozenia, planeta, gwiazda):
    fig, ax = plt.subplots(figsize=(8,8))
    star = plt.Circle((gwiazda.r), gwiazda.rad, color = 'blue')
    ax.add_artist(star)
    for i in xrange(liczba_iteracji):
        planet = plt.Circle((polozenia[i]), planeta.rad, color = 'g')
        ax.add_artist(planet)
    plt.show()
    plt.xlim(-1,4)
    plt.ylim(-2,2)
    fig.savefig('orbita.png')

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

c = raw_input('''Wybierz rodzaj symulacji:\n\
1 - Euler 2 - Verlet 3 - Leapfrog \n''')

if int(c) == 1:
    print 'jestem w 1'
    euler_start(polozenia, pedy, andrzej7000.r, andrzej7000.v, andrzej7000.m)
    euler(polozenia, pedy, liczba_iteracji, andrzej7000, czomberbomber123, kinetyczna, potencjaly)
elif int(c) == 2:
    print 'jestem w 2'
    verlet_start(andrzej7000.r, andrzej7000.v)
    verlet(polozenia, liczba_iteracji, andrzej7000, czomberbomber123, kinetyczna, potencjaly)
elif int(c) == 3:
    print 'jestem w 3'
    leapfrog_start(andrzej7000, predkosci, polozenia, czomberbomber123)
    leapfrog(liczba_iteracji, predkosci, polozenia, andrzej7000, czomberbomber123, kinetyczna, potencjaly)

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
star = plt.Circle((czomberbomber123.r), czomberbomber123.rad, color = 'blue')
ax.add_artist(star)
for i in xrange(liczba_iteracji):
    planet = plt.Circle((polozenia[i]), andrzej7000.rad, color = 'g')
    ax.add_artist(planet)
plt.xlim(-4,4)
plt.ylim(-4,4)
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(xrange(liczba_iteracji), potencjaly)
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(xrange(liczba_iteracji), kinetyczna)
ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(xrange(liczba_iteracji), map(add,potencjaly,kinetyczna))
plt.ylim(-0.18,-0.22)
plt.show()
