import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

a = 1
b = 1
c = 0.2
w = 0.2 * 2 * np.pi
f = 0.2

class wahadlo:
	def __init__ (self,pos,vel):
		self.x = pos
		self.v = vel

X = [u,v]

def dX_dt(X, t=0):
    return array([ X[1],
            b*X[0] - a*X[0]**3 - c*X[1] + f*np.cos(w*t)])

t = linspace(0, 15,  1000)              # time
X0 = array([10, 5])                     # initials conditions: 10 rabbits and 5 foxes
X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)
infodict['message']
rabbits, foxes = X.T
f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Rabbits')
p.plot(t, foxes  , 'b-', label='Foxes')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of fox and rabbit populations')
f1.savefig('rabbits_and_foxes_1.png')
