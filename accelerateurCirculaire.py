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
Variables d'initialisation
"""
c = 299_792_458  # c = constante de célérité de la lumière dans le vide en m/s
# r = int(input("Saisissez le rayon du cercle (en mètre): "))
rayon = 6400

vitesseTanSur_c_input = 0.9
v_tan_input = vitesseTanSur_c_input * c


dureeViePropre = 2.2E-6
v_t = np.linspace(0, 1, 1000)
dureeVieLaboTableau = []
distanceMoyenneTableau = []



def lancement_calcul():
    global c
    global vitesseTanSur_cValue
    v_tan_input = vitesseTanSur_cValue.get()*c

    # v_tan_input = 0.9*c
    global rayonValue
    global dureeViePropreValue

    # a0 = rayonValue.get()
    # duree_vie_propre = dureeViePropreValue.get()

    v_t = np.linspace(0, 0.999, 1000)           # 0.999 et pas 1 pour avoir un graphique lisible

    dureeVieLaboTableau = []
    distanceMoyenneTableau = []
    v_angulaireTableau = []

    for element in v_t:
        vitesse = element * c
        gamma = 1 / sqrt(1 - vitesse ** 2 / (c ** 2))
        v_angulaire = (vitesse / (rayonValue.get()*2*pi))     # vitesse angulaire en tours / s
        dureeVieMoyenneLabo = dureeViePropreValue.get() * gamma
        distanceMoyenne = vitesse * dureeVieMoyenneLabo
        dureeVieLaboTableau.append(dureeVieMoyenneLabo)
        distanceMoyenneTableau.append(distanceMoyenne)
        v_angulaireTableau.append(v_angulaire)

    # calcul en fonction de l'entrée de l'utilisateur
    gamma_v_input_case = 1 / sqrt(1 - v_tan_input ** 2 / (c ** 2))
    dureeVie_v_input_case = dureeViePropreValue.get() * gamma_v_input_case
    v_angulaire_input_case = (v_tan_input / (rayonValue.get() * 2 * pi))
    distanceMoyenne_input_case = v_tan_input * dureeVie_v_input_case


    fig = Figure()
    ax = fig.add_subplot(111, xlabel='Rapport vitesse tangentielle sur c : v_t/c',
                         ylabel='Durée de vie du muon en laboratoire (s)')
    ax.plot(v_t, dureeVieLaboTableau)
    print(v_tan_input / c)
    print(dureeVie_v_input_case)
    ax.plot(v_tan_input / c, dureeVie_v_input_case, marker="v", color="red")
    ax.grid(True)
    duree_vie_text = Label(win, text="Durée de vie estimée en laboratoire (s) : " + dureeVie_v_input_case.__str__())                       # afficher la durée de vie estimée
    duree_vie_text.grid(row=3, column=1)
    print(v_angulaire_input_case)
    print(distanceMoyenne_input_case)
    fig1 = Figure()
    ax1 = fig1.add_subplot(111, xlabel='Période de rotation (tours/s)', ylabel='Distance moyenne parcourue (en m)')
    ax1.plot(v_angulaireTableau, distanceMoyenneTableau)
    ax1.plot(v_angulaire_input_case, distanceMoyenne_input_case, marker="v", color="red")
    ax1.grid(True)
    # ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
    # ax2.plot(x, v_array)
    # ax2.grid(True)

    graph = FigureCanvasTkAgg(fig, master=win)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0, pady=0, columnspan=5)

    graph2 = FigureCanvasTkAgg(fig1, master=win)
    canvas2 = graph2.get_tk_widget()
    canvas2.grid(row=0, column=6)


# accelerateur_lineaire(c,v0,a,duree_vie_propre)

win = Tk()
win.title("Acceleration constante le long d'un axe")

vitesseTanSur_cVar = StringVar()
rayonVar = StringVar()
dureeViePropreVar = StringVar()

vitesseTanSur_cValue = DoubleVar()
rayonValue = DoubleVar()
dureeViePropreValue = DoubleVar()

vitesseTanSur_cValue.set(vitesseTanSur_c_input)
rayonValue.set(rayon)
dureeViePropreValue.set(dureeViePropre)

vitesseTanSur_cVar.set("Rapport vitesse tangentielle sur c : v_t/c")
rayonVar.set("Rayon (en m)")
dureeViePropreVar.set("Durée de vie (en s)")

vitesseTanSur_c_text = Label(win, text=vitesseTanSur_cVar.get())
rayon_text = Label(win, text=rayonVar.get())
dureeViePropre_text = Label(win, text=dureeViePropreVar.get())

vitesseTanSur_c_input = Entry(win, textvariable=vitesseTanSur_cValue)
rayon_input = Entry(win, textvariable=rayonValue)
dureeViePropre_input = Entry(win, textvariable=dureeViePropreValue)

calcul = Button(win, text='Calculer', command=lancement_calcul)
fig = Figure()
ax = fig.add_subplot(111, xlabel='Rapport vitesse tangentielle sur c : v_t/c ([0;1[)',
                     ylabel='Durée de vie du muon en laboratoire (s)')
ax.grid(True)

fig1 = Figure()
ax1 = fig1.add_subplot(111, xlabel='Période de rotation (tours/s)', ylabel='Distance moyenne parcourue (en m)')
ax1.grid(True)
# ax2 = fig1.add_subplot(212, xlabel='temps (s)', ylabel='vitesse (m/s)')
# ax2.grid(True)

graph = FigureCanvasTkAgg(fig, master=win)
graph2 = FigureCanvasTkAgg(fig1, master=win)
canvas = graph.get_tk_widget()
canvas2 = graph2.get_tk_widget()
canvas.grid(row=0, column=0, pady=0, columnspan=5)
canvas2.grid(row=0, column=6)
vitesseTanSur_c_text.grid(row=1, column=0)
rayon_text.grid(row=1, column=1)
dureeViePropre_text.grid(row=1, column=2)
vitesseTanSur_c_input.grid(row=2, column=0)
rayon_input.grid(row=2, column=1)
dureeViePropre_input.grid(row=2, column=2)
calcul.grid(row=1, column=3, pady=0, rowspan=2, columnspan=2)
win.mainloop()

# tracer l'esperance de vie en fonction des vitesses tangentielles
# tracer la distance moyenne parcourue en fonction de la période de rotation (nombre de tours) ou de la vitesse tangentielle
# Vous pouvez raffiner ce cas en supposant que la vitesse est augmentée d’une certaine quantité d’un tour à l’autre (vous pouvez vous inspirer du fonctionnement réel des accélérateurs circulaires).
# Dans cette situation, vous pouvez également tracer les graphes précédents.
