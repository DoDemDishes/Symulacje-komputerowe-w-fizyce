import matplotlib.pyplot as plt
import numpy as np

class czastka:
    """ Klasa opisujaca pojedyncza czastke gazu """
    def __init__(self,radius,pos,vel):
        self.rad = radius
        self.r = pos # polozenie
        self.v = vel # predkosc

gaz = [] # zbiornik na czastki
liczba_czastek = 100
c = plt.cm.summer(0.5)
fig, ax = plt.subplots( figsize=(8,8) )

for i in xrange(liczba_czastek):
    polozenie = np.array([np.random.uniform(0.,1.), np.random.uniform(0.,1.)])
    predkosc = np.array([np.random.uniform(0.,1.), np.random.uniform(0.,1.)])
    andrzej = czastka(0.02,polozenie,predkosc)
    gaz.append(andrzej)

for i in xrange(liczba_czastek):
    c = plt.cm.summer(np.linalg.norm(gaz[i].v))
    kolko = plt.Circle((gaz[i].r), 0.02, color = c)
    ax.add_artist(kolko)

fig.savefig('kolka.png')
