import numpy as np
import matplotlib.pyplot as plt
import math

t = 0
r = np.array([0,0])
points = list()

choice1 = input("Co rysujemy? \n 1 - Trojkaty Sierpinskieg \n 2 - Paprotki Barnsley'a \n")
choice2 = int(input("Liczba iteracji? \n"))

if choice1 == 1:
    def iteration(r,m):
        r = [m[0]*r[0] + m[1]*r[1] + m[4], m[2]*r[0] + m[3]*r[1] + m[5]]
        return r

    while t < choice2:
        ##generowanie liczby od 1 do 3
        random = np.random.randint(1,4)
        if random == 1:
            m = np.array([0.5,0,0,0.5,0,0])
            r = iteration(r,m)
            points.append(r)
        elif random == 2:
            m = np.array([0.5,0,0,0.5,0.5,0])
            r = iteration(r,m)
            points.append(r)
        else:
            m = np.array([0.5,0,0,0.5,0.25,math.sqrt(3.)/4])
            r = iteration(r,m)
            points.append(r)
        t += 1
elif choice1 == 2:
    def iteration(r,m):
        r = [m[0]*r[0] + m[1]*r[1] + m[4], m[2]*r[0] + m[3]*r[1] + m[5]]
        return r
    while t < choice2:
        ##generowanie liczby od 1 do 100
        random = np.random.randint(1,101)
        if random <= 73:
            m = [0.85, 0.04,-0.04, 0.85, 0.0, 1.6]
            r = iteration(r,m)
            points.append(r)
        elif random > 73 & random <= 86 :
            m = [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44]
            r = iteration(r,m)
            points.append(r)
        elif random > 86 & random <= 97:
            m = [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44]
            r = iteration(r,m)
            points.append(r)
        elif random > 97 & random <= 100:
            m = [ 0.0, 0.0, 0.0, 0.16, 0.0, 0.0]
            r = iteration(r,m)
            points.append(r)
        t += 1

else:
    print "Zly wybor, sprobuj jeszcze raz"


zip(*points)
plt.scatter(*zip(*points))
plt.show()
