##
# Commandes de base du langage Python
#

# Déclarer et affecter une variable
nombre = 4.5
prenom = "Jeffrey"

# Sorties à l'écran
print("Hello world")
print(nombre)
print("Bonjour", prenom)

# Entrées clavier
nom = input("Quel est votre nom ?")
age = int(input("Quel est votre age ?"))
taille = float(input("Quelle est votre taille en mètre ?"))

# Conditions
if age==0:
    print("Il doit y avoir une erreur !")
elif age<18:
    print("Vous êtes mineur")
else:
    print("Vous êtes majeur")

# Boucle "Tant que"
i = 0
while i<10:
    print(i)
    i = i+1

# Boucle "Pour"
for i in range(1,10):
    print(i)