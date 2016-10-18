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
promien = 0.02
fig, ax = plt.subplots(figsize=(8,8))

def losowanie (liczba_czastek, promien, tabela):
    for i in xrange(liczba_czastek):
        polozenie = np.array([np.random.uniform(0.,1.), np.random.uniform(0.,1.)])
        predkosc = np.array([np.random.uniform(0.,1.), np.random.uniform(0.,1.)])
        nakladanie = False
        for i in gaz:
            if ((i.r[0] - polozenie[0])**2 + (i.r[1] - polozenie[1])**2) < (2*promien)**2:
                nakladanie = True
                print 'najezdca'
        if nakladanie == False:
            andrzej = czastka(promien, polozenie, predkosc)
            gaz.append(andrzej)

while (len(gaz) < liczba_czastek):
    losowanie(liczba_czastek, promien, gaz)

for i in xrange(liczba_czastek):
    c = plt.cm.cool(np.linalg.norm(gaz[i].v))
    kolko = plt.Circle((gaz[i].r), promien, color = c)
    ax.add_artist(kolko)
fig.savefig('kolka.png')
print len(gaz)
for i in gaz:
    print i.r
plt.show()
