##
# Calcul du rendu de monnaie
#

montant = float(input("Montant à payer :"))
donne = float(input("Montant donné :"))

rendu = donne-montant

print("On doit rendre ",rendu," euros soit :")

# Pour éviter des erreurs d'arrondis :
rendu = rendu*100

# Billets de 5 euros
nb = int(rendu/500)
rendu = rendu-nb*500
print(nb," billets de 5 euros")

# Pièces de 2 euros
nb = int(rendu/200)
rendu = rendu-nb*200
print(nb," pièces de 2 euros")

# Pièces de 1 euros
nb = int(rendu/100)
rendu = rendu-nb*100
print(nb," pièces de 1 euros")

# Pièces de 50 cents
nb = int(rendu/50)
rendu = rendu-nb*50
print(nb," pièces de 50 cents")

# Pièces de 10 cents
nb = int(rendu/10)
rendu = rendu-nb*10
print(nb," pièces de 10 cents")


# Pièces de 5 cents
nb = int(rendu/5)
rendu = rendu-nb*5
print(nb," pièces de 5 cents")

if rendu>0:
    print("Je garde le reste !")