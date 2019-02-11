##
# Vérification qu'un nombre est premier ou non
#

nb = int(input("Saisissez un nombre : "))

i = 2
nbDiv = 0

while i<nb:
    if nb % i == 0:
        nbDiv = nbDiv+1
    i = i+1

if nbDiv==0:
    print("Le nombre est premier")
else:
    print("Le nombre n'est pas premier")