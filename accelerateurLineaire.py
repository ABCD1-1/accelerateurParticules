import matplotlib.pyplot as plt
import numpy as np
from math import acos,exp
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure

def onCLick():
    return

def accelerateur_lineaire(c,v0,a0,duree_vie_propre):
    x = np.linspace(0,10,100000)
    a_array = []
    v_array = []
    tempsPropre = []

    for elt in x:
        a = acceleration(elt,a0)
        a_array.append(a)
        v_array.append(vitesse(elt,v0))
        tempsPropre.append(temps_propre(elt,a))
    
    plt.figure(0)
    plt.subplot(211)
    plt.plot(x,a_array)
    plt.xlabel('temps (s)')
    plt.ylabel('acceleration (m/s2)')
    plt.subplot(212)
    plt.plot(x,v_array)
    plt.xlabel('temps (s)')
    plt.ylabel('vitesse (m/s)')

    fig = Figure()
    ax = fig.add_subplot(111, xlabel='v0 (m/s2)', ylabel='espérance de vie (s)')
    ax.plot(x,a_array)
    ax.grid(True)

    graph = FigureCanvasTkAgg(fig, master=win)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0, pady=0, columnspan = 4)


#def vitesse(a,t,v0,c):
#    return (a*t)/(1+(a*t/c)**2)**(1/2)

def temps_propre(t,a):
    return (c/a)*acos(a*t/c)

#def position(c,a,t):
#    return (c**2/a)*(1+((a*t)/c)**2)**(1/2)

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

#accelerateur_lineaire(c,v0,a,duree_vie_propre)

win = Tk()
win.title("Acceleration constante le long d'un axe")

celeriteVar = StringVar()
vitesseIniVar = StringVar()
accelerationVar = StringVar()
tPropreVar = StringVar()

celeriteVar.set("Célérité")
vitesseIniVar.set("Vitesse initiale")
accelerationVar.set("Accélération")
tPropreVar.set("Temps propre")

celerite_text = Label(win, text = celeriteVar.get())
vitesseIni_text = Label(win, text = vitesseIniVar.get())
acceleration_text = Label(win, text = accelerationVar.get())
tPropre_text = Label(win, text = tPropreVar.get())

celerite_input = Entry(win)
vitesseIni_input = Entry(win)
acceleration_input = Entry(win)
tPropre_input = Entry(win)

calcul = Button(win, text='Calculer')
fig = Figure()
ax = fig.add_subplot(111)
ax.grid(True)

graph = FigureCanvasTkAgg(fig, master=win)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0, pady=0, columnspan = 4)
celerite_text.grid(row=1, column=0)
vitesseIni_text.grid(row=1, column=1)
acceleration_text.grid(row=1, column=2)
tPropre_text.grid(row=1, column=3)
celerite_input.grid(row=2, column=0)
vitesseIni_input.grid(row=2, column=1)
acceleration_input.grid(row=2, column=2)
tPropre_input.grid(row=2, column=3)
calcul.grid(row = 3, column = 0, pady=0, columnspan = 4)
win.mainloop()


