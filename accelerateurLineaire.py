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

def accelerateur_lineaire():
    global c
    global vitesseIniValue
    global accelerationValue
    global tPropreValue

    v0 = vitesseIniValue.get()
    a0 = accelerationValue.get()
    duree_vie_propre = tPropreValue.get()

    x = np.linspace(0,10,100)
    a_array = []
    v_array = []
    tempsPropre = []

    for elt in x:
        a = acceleration(elt,a0)
        a_array.append(a)
        v_array.append(vitesse(elt,v0))
        tempsPropre.append(temps_propre(elt,a,c))
    
    fig1 = Figure()
    ax1 = fig1.add_subplot(211, xlabel='temps (s)', ylabel='acceleration (m/s2)' )
    ax1.plot(x,a_array)
    ax1.grid(True)
    ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
    ax2.plot(x,v_array)
    ax2.grid(True)

    fig = Figure()
    ax = fig.add_subplot(111, xlabel='v0 (m/s2)', ylabel='espérance de vie (s)')
    ax.plot(x,v_array)
    ax.grid(True)

    graph = FigureCanvasTkAgg(fig, master=win)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0, pady=0, columnspan = 5)

    graph2 = FigureCanvasTkAgg(fig1, master=win)
    canvas2 = graph2.get_tk_widget()
    canvas2.grid(row=0, column=6)




#def vitesse(a,t,v0,c):
#    return (a*t)/(1+(a*t/c)**2)**(1/2)

def temps_propre(t,a,c):
    return (c/a)*acos(a*t/c)

#def position(c,a,t):
#    return (c**2/a)*(1+((a*t)/c)**2)**(1/2)

def acceleration(t,a):
    print(exp(-t))
    return a*exp(-t)+5e-324

def vitesse(t,v0):
    return (c-v0)*(1-exp(-t))+v0

c = 299_792_458
v0 = 0.9*c
a = 9.81
duree_vie_propre = 2.2E-6
t=0

#accelerateur_lineaire(c,v0,a,duree_vie_propre)

win = Tk()
win.title("Acceleration constante le long d'un axe")

vitesseIniVar = StringVar()
accelerationVar = StringVar()
tPropreVar = StringVar()

vitesseIniValue = DoubleVar()
accelerationValue = DoubleVar()
tPropreValue = DoubleVar()

vitesseIniValue.set(v0)
accelerationValue.set(a)
tPropreValue.set(duree_vie_propre)

vitesseIniVar.set("Vitesse initial")
accelerationVar.set("Accélération")
tPropreVar.set("Temps propre")

vitesseIni_text = Label(win, text = vitesseIniVar.get())
acceleration_text = Label(win, text = accelerationVar.get())
tPropre_text = Label(win, text = tPropreVar.get())

vitesseIni_input = Entry(win, textvariable = vitesseIniValue)
acceleration_input = Entry(win, textvariable = accelerationValue)
tPropre_input = Entry(win, textvariable = tPropreValue)

calcul = Button(win, text='Calculer', command=accelerateur_lineaire)
fig = Figure()
ax = fig.add_subplot(111)
ax.grid(True)

fig1 = Figure()
ax1 = fig1.add_subplot(211, xlabel='temps (s)', ylabel='acceleration (m/s2)' )
ax1.grid(True)
ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
ax2.grid(True)

graph = FigureCanvasTkAgg(fig, master=win)
graph2 = FigureCanvasTkAgg(fig1, master=win)
canvas = graph.get_tk_widget()
canvas2 = graph2.get_tk_widget()
canvas.grid(row=0, column=0, pady=0, columnspan = 5)
canvas2.grid(row=0, column=6)
vitesseIni_text.grid(row=1, column=0)
acceleration_text.grid(row=1, column=1)
tPropre_text.grid(row=1, column=2)
vitesseIni_input.grid(row=2, column=0)
acceleration_input.grid(row=2, column=1)
tPropre_input.grid(row=2, column=2)
calcul.grid(row = 1, column = 3, pady=0, rowspan = 2, columnspan = 2)
win.mainloop()


