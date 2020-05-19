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
c = 299_792_458
rayon = 6400
vitesseTanSur_c_input = 0.9
v_tan_input = vitesseTanSur_c_input * c
dureeViePropre = 2.2E-6


def lancement_calcul():
    global c
    global vitesseTanSur_cValue
    v_tan_input = vitesseTanSur_cValue.get()*c
    global rayonValue
    global dureeViePropreValue

    v_t = np.linspace(0, 0.999, 1000)           # 0.999 et pas 1 pour avoir un graphique lisible
    dureeVieLaboTableau = []
    distanceMoyenneTableau = []
    periode_rotationTableau = []

    for element in v_t:
        vitesse = element * c
        gamma = 1 / sqrt(1 - vitesse ** 2 / (c ** 2))
        dureeVieMoyenneLabo = dureeViePropreValue.get() * gamma
        distanceMoyenne = vitesse * dureeVieMoyenneLabo
        dureeVieLaboTableau.append(dureeVieMoyenneLabo)
        distanceMoyenneTableau.append(distanceMoyenne)
        if(vitesse!=0):
            periode_rotation = 2*pi*rayonValue.get() / vitesse
            periode_rotationTableau.append(periode_rotation)
        else:
            periode_rotationTableau.append(0)

    # calcul en fonction de l'entrée de l'utilisateur
    gamma_v_input_case = 1 / sqrt(1 - v_tan_input ** 2 / (c ** 2))
    dureeVie_v_input_case = dureeViePropreValue.get() * gamma_v_input_case
    distanceMoyenne_input_case = v_tan_input * dureeVie_v_input_case
    periode_rotation_input = 2 * pi * rayonValue.get() / v_tan_input

    nombre_tours_input_case = distanceMoyenne_input_case / (rayonValue.get() * 2 * pi)

    fig = Figure()
    ax = fig.add_subplot(111, xlabel='Rapport vitesse tangentielle sur c : v_t/c',
                         ylabel='Durée de vie du muon en laboratoire (s)')
    ax.plot(v_t, dureeVieLaboTableau)
    print("Durée de vie : ",dureeVie_v_input_case)
    ax.plot(v_tan_input / c, dureeVie_v_input_case, marker="v", color="red")
    ax.grid(True)
    duree_vie_text = Label(win, text="Durée de vie estimée en laboratoire (s) : " + dureeVie_v_input_case.__str__())                       # afficher la durée de vie estimée
    duree_vie_text.grid(row=3, column=1)
    print("Distance moyenne parcourue (en m): ",distanceMoyenne_input_case)
    print("Distance moyenne parcourue en nombre de tours : ",nombre_tours_input_case)
    fig1 = Figure()
    ax1 = fig1.add_subplot(111, xlabel='Période de rotation (s)', ylabel='Distance moyenne parcourue (en m)')
    ax1.plot(periode_rotationTableau, distanceMoyenneTableau)
    ax1.plot(periode_rotation_input, distanceMoyenne_input_case, marker="v", color="red")
    ax1.grid(True)

    distance_text = Label(win, text="Distance parcourue estimée (m) : " + distanceMoyenne_input_case.__str__())                       # afficher la durée de vie estimée
    distance_text.grid(row=2, column=6)
    nb_tour_text = Label(win, text="Distance parcourue estimée en nombre de tours : " + nombre_tours_input_case.__str__())            # afficher la distance parcourue en nombre de tours
    nb_tour_text.grid(row=3, column=6)
    graph = FigureCanvasTkAgg(fig, master=win)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0, pady=0, columnspan=5)

    graph2 = FigureCanvasTkAgg(fig1, master=win)
    canvas2 = graph2.get_tk_widget()
    canvas2.grid(row=0, column=6)

win = Tk()
win.title("Simulation de la durée de vie d'un muon : mouvement circulaire uniforme")

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
ax1 = fig1.add_subplot(111, xlabel='Période de rotation (s)', ylabel='Distance moyenne parcourue (en m)')
ax1.grid(True)

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

