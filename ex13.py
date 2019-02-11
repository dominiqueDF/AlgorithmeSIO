##
# Jeu de la devinette
#

import random

nb = int(random.randint(1,100))

nbCoup = 0
proposition = 0

while nbCoup<10 and proposition!=nb:
    proposition = int(input("Votre proposition :"))
    if proposition>nb:
        print("Trop grand")
    elif proposition<nb:
        print("Trop petit")
    else:
        print("Gagné !")
    nbCoup = nbCoup+1

if nb!=proposition:
    print("Perdu ! Il fallait trouver ",nb)
