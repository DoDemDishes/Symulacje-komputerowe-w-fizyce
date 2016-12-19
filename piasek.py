import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
from collections import Counter

dim = (100,100)
mapa = np.zeros(dim)
t = 0
tmax = 30000
temp = []
liczba_czastek = []
falaaaa = []
stacjonarny = False

while t < tmax:
        fala = 0
        while 1:
            test = False
            for i in xrange(dim[0]):
                for j in xrange(dim[1]):
                    if mapa[i][j] >= 4:
                        temp.append(np.array([i,j]))
                        mapa[i][j] -= 4
                        test = True
            for i in xrange(len(temp)):
                try:
                    mapa[temp[i][0]+1][temp[i][1]] += 1
                except IndexError:
                    pass
                try:
                    mapa[temp[i][0]-1][temp[i][1]] += 1
                    if temp[i][0]-1 < 0:
                        raise IndexError
                except IndexError:
                    pass
                try:
                    mapa[temp[i][0]][temp[i][1]+1] += 1
                except IndexError:
                    pass
                try:
                    mapa[temp[i][0]][temp[i][1]-1] += 1
                    if temp[i][1]-1 < 0:
                        raise IndexError
                except IndexError:
                    pass
            temp = []
            fala += 1
            if test == False: break
        if stacjonarny == True:
            falaaaa.append(fala)
        x = np.random.randint(0,dim[0])
        y = np.random.randint(0,dim[1])
        mapa[x][y] += 1
        t += 1
        liczba_czastek.append([t,np.array([np.sum(mapa)])])
        if t >= 22500:
            stacjonarny = True
wystepowanie = Counter(falaaaa)
### printowanie macierzy
# print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#       for row in mapa]))
### printowanie mapy
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('Height of the Sandpile')
cax = ax.imshow(mapa, interpolation='nearest')
cax.set_clim(vmin=0, vmax=5)
cbar = fig.colorbar(cax, ticks=[0,1,2,3,4,5], orientation='vertical')
filename = str('%03d' % t) + '.png'
plt.savefig(filename, dpi=100)
plt.clf()
### printowanie liczby czastek od czasu
plt.plot(*zip(*liczba_czastek))
plt.xlabel('czas')
plt.ylabel('liczba czastek')
plt.savefig(str('%03d' % t)+'czastki_od_czasu.png')
plt.clf()
### printowanie histogramu
ax = plt.gca()
ax.plot(wystepowanie.keys(),wystepowanie.values())
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('S')
plt.ylabel('N(S)')
plt.savefig(str('%03d' % t)+'loglog.png')
### zapisywanie do csv
with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in wystepowanie.items():
       writer.writerow([key, value])
