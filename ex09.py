##
# Calcul du produit des entiers entre
# deux nombres
#

depart = int(input("Nombre de départ :"))
fin = int(input("Nombre de fin :"))

produit = 1
for i in range(depart,fin+1):
    produit = produit*i

print("Le produit vaut ",produit)