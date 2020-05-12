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
# r = rayon du mouvement circulaire en m
# dureeViePropre = durée de vie propre moyenne d'un muon (de sa naissance à sa désintégration)
# dureeVieMoyenneLabo = durée de vie moyenne dans le labo en seconde
# distanceMoyenne = durée de vie moyenne dans le labo en seconde

from math import pi, sqrt

c = 299_792_458           # c = constante de célérité de la lumière dans le vide en m/s
v0 = 0.9*c                # mouvement circulaire dont le rayon ne varie pas v = v_t
r = 6400                  # doit etre modifiable
v_t = v0                  # doit etre modifiable et constante, donc pas d'accélérateur tangentiel
dureeViePropre = 2E-6     # doit etre modifiable
gamma = 1/sqrt(1-v_t**2/(c**2))

v_angulaire = v_t/r
a_n = -v_t*v_t/r


dureeVieMoyenneLabo = dureeViePropre*gamma       # à déterminer
distanceMoyenne = v_t*dureeVieMoyenneLabo       # à déterminer
print("Durée de vie en labo (en secondes) : ",dureeVieMoyenneLabo)
print("\nDistance moyenne parcourue en mètre : ",distanceMoyenne)

# tracer l'esperance de vie en fonction des vitesses tangentielles

# voir les équations


