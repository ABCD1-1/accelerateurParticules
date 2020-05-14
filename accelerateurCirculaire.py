# mouvement circulaire uniforme
# Vous raisonnez avec un accélérateur circulaire (rayon R).
# Tracer l’espérance de vie de la particule considérée mesurée dans le laboratoire (par exemple pour un muon mais ce sera une particule hypothétique
# qui se désintègre en moyenne au bout de xx secondes dans son référentiel propre) en fonction de sa vitesse tangentielle (constante)
# à partir d'un point où elle est créée et où sa vitesse est v0.
# Tracer également la distance moyenne parcourue par la particule dans le laboratoire en fonction de la période de rotation ou de la vitesse tangentielle.
# Vous pouvez l’exprimer en nombre de tours.

# Les paramètres que vous pouvez faire varier sont :
# la durée de vie propre moyenne de la particule, le rayon R et la vitesse tangentielle pour le cas 2.
# Vous pouvez en choisir d’autres.
# Une fois ces paramètres entrés, vous afficherez comme résultats la durée de vie moyenne dans le labo
# et la distance moyenne parcourue dans le labo.

# a = a_n Or + a_t Ot
# a = -R*v_angulaire² Or (Axe rayon)        +   R d/dt(v_angulaire) Ot (Axe tangentiel)        si uniforme, d/dt(v_angulaire) = 0
# v = R * v_angulaire

# a_n = accélérateur normal
# a_t = accélérateur tangentiel
# v0 = vitesse initiale
# v_t = vitesse tangentielle
# v_angulaire = vitesse angulaire
# r = rayon du mouvement circulaire en mètre
# dureeViePropre = durée de vie propre moyenne d'un muon (de sa naissance à sa désintégration)
# dureeVieMoyenneLabo = durée de vie moyenne dans le labo en seconde
# distanceMoyenne = durée de vie moyenne dans le labo en seconde

import numpy as np
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure
from math import pi, sqrt
"""
Variables
"""
c = 299_792_458           # c = constante de célérité de la lumière dans le vide en m/s
# r = int(input("Saisissez le rayon du cercle (en mètre): "))
rayon = 6400                  # doit etre modifiable
# v0 = float(input("Saisissez le rapport vitesse du muon / celerite de la lumière :\n(exemple 0.9 pour une vitesse de 0.9*c) "))*c
v0 = 0.9*c
#dureeViePropre = float(input("Saisissez la durée de vie d'un muon en microseconde :\n(exemple 6 pour une durée de de 6 µs"))
dureeViePropre = 2.2E-6     # doit etre modifiable
v_t = np.linspace(0,1,1000)
dureeVieLaboTableau = []
distanceMoyenneTableau = []

for i in range(len(v_t)):
    vitesse = v_t[i]*c-0.000001           # -0.000001 pour éviter l'erreur de division par 0
    gamma = 1/sqrt(1-vitesse**2/(c**2))
    v_angulaire = vitesse / rayon
    a_n = -vitesse**2 / rayon
    dureeVieMoyenneLabo = dureeViePropre*gamma       # à déterminer
    distanceMoyenne = vitesse*dureeVieMoyenneLabo       # à déterminer
    dureeVieLaboTableau.append(dureeVieMoyenneLabo)
    distanceMoyenneTableau.append(distanceMoyenne)
    #print("Durée de vie en labo (en secondes) : ",dureeVieMoyenneLabo)
    #print("\nDistance moyenne parcourue en mètre : ",distanceMoyenne)

print(len(dureeVieLaboTableau))
print(dureeVieLaboTableau)
print(distanceMoyenneTableau)


def accelerateur_lineaire():
    global c
    global vitesseIniValue
    global rayonValue
    global dureeViePropreValue

    v0 = vitesseIniValue.get()
    a0 = rayonValue.get()
    duree_vie_propre = dureeViePropreValue.get()

    x = np.linspace(0, 10, 100)
    a_array = []
    v_array = []
    tempsPropre = []

    # for elt in x:
        # a = acceleration(elt, a0)
        # a_array.append(a)
        # v_array.append(vitesse(elt, v0))
        # tempsPropre.append(temps_propre(elt, a, c))

    fig1 = Figure()
    ax1 = fig1.add_subplot(211, xlabel='temps (s)', ylabel='acceleration (m/s2)')
    ax1.plot(x, a_array)
    ax1.grid(True)
    ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
    ax2.plot(x, v_array)
    ax2.grid(True)

    fig = Figure()
    ax = fig.add_subplot(111, xlabel='v0 (m/s2)', ylabel='espérance de vie (s)')
    ax.plot(x, v_array)
    ax.grid(True)

    graph = FigureCanvasTkAgg(fig, master=win)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0, pady=0, columnspan=5)

    graph2 = FigureCanvasTkAgg(fig1, master=win)
    canvas2 = graph2.get_tk_widget()
    canvas2.grid(row=0, column=6)





# accelerateur_lineaire(c,v0,a,duree_vie_propre)

win = Tk()
win.title("Acceleration constante le long d'un axe")

vitesseIniVar = StringVar()
rayonVar = StringVar()
dureeViePropreVar = StringVar()

vitesseIniValue = DoubleVar()
rayonValue = DoubleVar()
dureeViePropreValue = DoubleVar()

vitesseIniValue.set(v0)
rayonValue.set(rayon)
dureeViePropreValue.set(dureeViePropre)

vitesseIniVar.set("Vitesse initiale (en m/s)")
rayonVar.set("Rayon (en m)")
dureeViePropreVar.set("Durée de vie (en s)")

vitesseIni_text = Label(win, text=vitesseIniVar.get())
rayon_text = Label(win, text=rayonVar.get())
dureeViePropre_text = Label(win, text=dureeViePropreVar.get())

vitesseIni_input = Entry(win, textvariable=vitesseIniValue)
rayon_input = Entry(win, textvariable=rayonValue)
dureeViePropre_input = Entry(win, textvariable=dureeViePropreValue)

calcul = Button(win, text='Calculer', command=accelerateur_lineaire)
fig = Figure()
ax = fig.add_subplot(111)
ax.grid(True)

fig1 = Figure()
ax1 = fig1.add_subplot(211, xlabel='temps (s)', ylabel='acceleration (m/s2)')
ax1.grid(True)
ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
ax2.grid(True)

graph = FigureCanvasTkAgg(fig, master=win)
graph2 = FigureCanvasTkAgg(fig1, master=win)
canvas = graph.get_tk_widget()
canvas2 = graph2.get_tk_widget()
canvas.grid(row=0, column=0, pady=0, columnspan=5)
canvas2.grid(row=0, column=6)
vitesseIni_text.grid(row=1, column=0)
rayon_text.grid(row=1, column=1)
dureeViePropre_text.grid(row=1, column=2)
vitesseIni_input.grid(row=2, column=0)
rayon_input.grid(row=2, column=1)
dureeViePropre_input.grid(row=2, column=2)
calcul.grid(row=1, column=3, pady=0, rowspan=2, columnspan=2)
win.mainloop()

# tracer l'esperance de vie en fonction des vitesses tangentielles


