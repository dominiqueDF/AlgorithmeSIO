##
# Recherche de nombres premiers inférieurs à un nombre donné
#

nb = int(input("Saisissez un nombre : "))

nbaTester = 2

while nbaTester<=nb:
    i = 2
    nbDiv = 0

    while i<nbaTester:
        if nbaTester % i == 0:
            nbDiv = nbDiv+1
        i = i+1

    if nbDiv==0:
        print(nbaTester)

    nbaTester = nbaTester+1