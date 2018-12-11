##
# Calcul d'une heure d'arrivée
#

hd = int(input("Heure de départ :"))
md = int(input("Minutes de départ :"))
ht = int(input("Heures de trajet :"))
mt = int(input("Minutes de trajet :"))

timeD = hd+md/60
timeT = ht+mt/60

timeA = timeD+timeT

if timeA>24:
    lendemain=True
    timeA = timeA-24
else:
    lendemain=False

ha = int(timeA)
ma = int((timeA-ha)*60)

if lendemain:
    print("Vous arrivez demain à ",ha," heures ",ma)
else:
    print("Vous arrivez à ",ha," heures ",ma)
