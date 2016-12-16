import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.path as mplPath

t = 0
r = np.array([0,0])
points = list()
dimensions = list()

def iteration(r,m):
    r = [m[0]*r[0] + m[1]*r[1] + m[4], m[2]*r[0] + m[3]*r[1] + m[5]]
    return r

def generate_net(points, k):
    net = list()
    x_coordinates = np.array(np.linspace(min(zip(*points)[0]) , max(zip(*points)[0]), k))
    y_coordinates = np.array(np.linspace(min(zip(*points)[1]) , max(zip(*points)[1]), k))

    net.append(x_coordinates)
    net.append(y_coordinates)
    # print net
    return net

choice1 = input("Co rysujemy? \n 1 - Trojkaty Sierpinskiego \n 2 - Paprotki Barnsley'a \n")
choice2 = int(input("Liczba iteracji? \n"))

if choice1 == 1:
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
    while t < choice2:
        ##generowanie liczby od 1 do 100
        random = np.random.random()
        if random < 0.73:
            m = [0.85, 0.04,-0.04, 0.85, 0.0, 1.6]
            r = iteration(r,m)
            points.append(r)
        elif random < 0.86 :
            m = [0.2, -0.26, 0.23, 0.22, 0.0, 1.6]
            r = iteration(r,m)
            points.append(r)
        elif random < 0.97:
            m = [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44]
            r = iteration(r,m)
            points.append(r)
        else:
            m = [ 0.0, 0.0, 0.0, 0.16, 0.0, 0.0]
            r = iteration(r,m)
            points.append(r)
        t += 1
else:
    print "Zly wybor, sprobuj jeszcze raz"

## Liczenie rozmiaru pudelkowego
# for k in xrange(1,7):
#     nk = 0
#     for i in xrange(0,int(math.pow(2,k))):
#         for j in xrange(0,int(math.pow(2,k))):
#             # print 'i: ', i, ' j: ', j
#             includes = False
#             net = generate_net(points, math.pow(2,k)+1)
#             # print net
#             poly = [net[0][i],net[0][i+1],net[1][j],net[1][j+1]]
#             # print poly
#             bbPath = mplPath.Path(np.array([[poly[0], poly[1]],
#                          [poly[1], poly[2]],
#                          [poly[2], poly[3]],
#                          [poly[3], poly[0]]]))
#             for z in xrange(choice2):
#                 includes = bbPath.contains_point((points[z][0], points[z][1]))
#                 if includes == True:
#                     nk += 1
#                     break
#     dimensions.append([math.log(nk), k*math.log(2)])

# np.savetxt("Paprotki_100k.csv", dimensions, delimiter=",")
# zip(*points)
# plt.figure(1)
plt.plot(*zip(*points), s = 1 )
# plt.subplot(212)
# plt.scatter(*zip(*dimensions))
plt.show()
