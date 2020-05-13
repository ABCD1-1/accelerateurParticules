import matplotlib.pyplot as plt
import numpy as np
from math import acos

def accelerateur_lineaire(c,v0,a,duree_vie_propre):
    y = []
    x = np.linspace(0,1,100000)
    for elt in x:
        y.append(vitesse(a,elt,v0,c))
    plt.plot(x,y)
    plt.xlabel('temps (s)')
    plt.ylabel('vitesse (m/s)')
    plt.show()
    return 

def vitesse(a,t,v0,c):
    return (a*t)/(1+(a*t/c)**2)**(1/2)

def temps_propre(c,a,t):
    return (c/a)*acos(a*t/c)

def position(c,a,t):
    return (c**2/a)*(1+((a*t)/c)**2)**(1/2)

g = 9.81
c = 299_792_458
v0 = 0.9*c
a = g
duree_vie_propre = 2.2E-6
t=0

#accelerateur_lineaire(c,v0,a,duree_vie_propre)
print(vitesse(a,1,v0,c))
