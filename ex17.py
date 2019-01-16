##
# Génération d'un numéro de carte bleue
#

# On part d'un numéro "vide"
numero = ""

# Première étape : On génére "aléatoirement" les 15 premiers chiffres
import random

i = 0
while i<15:
    # On génère un chiffre entre 0 et 9
    chiffre = random.randint(0,9)
    # On concatène le chiffre au numéro
    numero = numero + str(chiffre)
    i = i + 1

# Calcul de la clef sur les 15 premiers chiffres
# Ceci aurait pu être fait dans la même boucle que précédemment
total = 0
i = 0
while i<15:
    # Chiffre en position paire
    if i%2 == 0:
        total = total + 2*int(numero[i])
        if int(numero[i])>4:
            total = total+1
    # Chiffre en position impaire
    else:
        total = total + int(numero[i])
    i = i + 1

# Calcul du dernier chiffre
dernier = 10 - total%10

numero = numero+str(dernier)

print(numero)