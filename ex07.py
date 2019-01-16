##
# Affichage des entiers entre deux nombres
#

depart = int(input("Nombre de départ :"))
fin = int(input("Nombre de fin :"))

# Version boucle "pour"
for i in range(depart,fin+1):
    print(i)

# Version boucle "tant que"
i = depart
while i<=fin:
    print(i)
    i=i+1
