import matplotlib.pyplot as plt
import numpy as np
from math import acos,exp

def accelerateur_lineaire(c,v0,a,duree_vie_propre):
    x = np.linspace(0,10,100000)
    a_array = []
    v_array = []

    for elt in x:
        a_array.append(acceleration(elt,a))
        v_array.append(vitesse(elt,v0))
    
    plt.subplot(211)
    plt.plot(x,a_array)
    plt.xlabel('temps (s)')
    plt.ylabel('acceleration (m/s2)')
    plt.subplot(212)
    plt.plot(x,v_array)
    plt.xlabel('temps (s)')
    plt.ylabel('vitesse (m/s)')
    plt.show()
    return 

#def vitesse(a,t,v0,c):
#    return (a*t)/(1+(a*t/c)**2)**(1/2)

def temps_propre(c,a,t):
    return (c/a)*acos(a*t/c)

def position(c,a,t):
    return (c**2/a)*(1+((a*t)/c)**2)**(1/2)

def acceleration(t,a):
    return a*exp(-t)

def vitesse(t,v0):
    return (c-v0)*(1-exp(-t))+v0

g = 9.81
c = 299_792_458
v0 = 0.9*c
a = g
duree_vie_propre = 2.2E-6
t=0

accelerateur_lineaire(c,v0,a,duree_vie_propre)
#print(vitesse(a,1,v0,c))


