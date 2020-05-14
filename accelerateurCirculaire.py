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

from tkinter import *
from math import pi, sqrt

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure
import numpy as np

"""
Variables
"""
c = 299_792_458           # c = constante de célérité de la lumière dans le vide en m/s
# r = int(input("Saisissez le rayon du cercle (en mètre): "))
r = 6400                  # doit etre modifiable
# v0 = float(input("Saisissez le rapport vitesse du muon / celerite de la lumière :\n(exemple 0.9 pour une vitesse de 0.9*c) "))*c
v0 = 0.9*c                # doit etre modifiable
# dureeViePropre = float(input("Saisissez la durée de vie d'un muon en microseconde :\n(exemple 6 pour une durée de de 6 µs"))
dureeViePropre = 2.2E-6     # doit etre modifiable
v_t = np.linspace(0,1,1000)
dureeVieLaboTableau = []
distanceMoyenneTableau = []
for i in range(len(v_t)):
    vitesse = v_t[i]*c-0.000001           # -0.000001 pour éviter l'erreur de division par 0
    gamma = 1/sqrt(1-vitesse**2/(c**2))
    v_angulaire = vitesse/r
    a_n = -vitesse**2/r
    dureeVieMoyenneLabo = dureeViePropre*gamma       # à déterminer
    distanceMoyenne = vitesse*dureeVieMoyenneLabo       # à déterminer
    dureeVieLaboTableau.append(dureeVieMoyenneLabo)
    distanceMoyenneTableau.append(distanceMoyenne)
    # print("Durée de vie en labo (en secondes) : ",dureeVieMoyenneLabo)
    # print("\nDistance moyenne parcourue en mètre : ",distanceMoyenne)

print(len(dureeVieLaboTableau))
print(dureeVieLaboTableau)
print(distanceMoyenneTableau)

win = Tk()
win.title("Mouvement circulaire uniforme")

vitesseIniVar = StringVar()
rayonVar = StringVar()
dureeViePropreVar = StringVar()

vitesseIniVar.set("Vitesse initiale en rapport v0/c")
rayonVar.set("Rayon (en m)")
dureeViePropreVar.set("Durée de vie propre (en s)")

vitesseIni_text = Label(win, text = vitesseIniVar.get())
rayon_text = Label(win, text = rayonVar.get())
dureeViePropre_text = Label(win, text = dureeViePropreVar.get())

vitesseIni_input = Entry(win)
rayon_input = Entry(win)
dureeViePropre_input = Entry(win)

calcul = Button(win, text='Calculer')
fig = Figure()
ax = fig.add_subplot(111)
ax.grid(True)

graph = FigureCanvasTkAgg(fig, master=win)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0, pady=0, columnspan = 4)
vitesseIni_text.grid(row=1, column=1)
rayon_text.grid(row=1, column=2)
dureeViePropre_text.grid(row=1, column=3)
vitesseIni_input.grid(row=2, column=1)
rayon_input.grid(row=2, column=2)
dureeViePropre_input.grid(row=2, column=3)
calcul.grid(row = 3, column = 0, pady=0, columnspan = 4)  # regrouper plusieurs cellules d’une ligne via columnspan, pady = marge externe verticale
win.mainloop()


# tracer l'esperance de vie en fonction des vitesses tangentielles



