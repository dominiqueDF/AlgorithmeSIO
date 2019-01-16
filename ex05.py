##
# Calcul d'un temps de trajet
#

hd = int(input("Heure de départ :"))
md = int(input("Minutes de départ :"))
ha = int(input("Heure d'arrivée :"))
ma = int(input("Minutes d'arrivée :"))

timeD = hd+md/60
timeA = ha+ma/60

if timeA<timeD: 
    timeA=timeA+24

timeT = timeA-timeD

ht = int(timeT)
mt = int((timeT-ht)*60)

print("Le trajet dure ",ht," heures ",mt)

