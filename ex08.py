##
# Calcul de la somme des entiers entre
# deux nombres
#

depart = int(input("Nombre de départ :"))
fin = int(input("Nombre de fin :"))

somme = 0
for i in range(depart,fin+1):
    somme = somme+i

print("La somme vaut ",somme)