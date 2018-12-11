##
# Affichage de l'année de majorité après saisie
# de l'année de naissance et année actuelle
#

anneeActuelle = int(input("En quelle année sommes-nous ? "))
anneeNaissance = int(input("En quelle année êtes-vous né ? "))
anneeMajorite = anneeNaissance+18

if anneeActuelle==anneeMajorite:
    print("Vous êtes majeur cette année !")
elif anneeActuelle>anneeMajorite:
    print("Vous êtes majeur !")
else:
    print("Vous serez majeur en ", anneeMajorite)
    if anneeMajorite-anneeActuelle>1:
        print("soit dans ", anneeMajorite-anneeActuelle, " ans")
    else:
        print("soit dans 1 an")
