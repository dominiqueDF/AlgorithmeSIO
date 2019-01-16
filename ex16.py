##
# Validation d'un numéro de carte bleue
#

numero = input("Saisissez un numéro de carte bleue : ")

# On vérifie que l'on a 16 caractères et réitère la saisie si nécessaire
while len(numero) != 16:
    numero = input("Saisissez un numéro de carte bleue (16 chiffres) : ")

# Calcul de la clef
total = 0
i = 0
while i<16:
    # Chiffre en position paire
    if i%2 == 0:
        total = total + 2*int(numero[i])
        if int(numero[i])>4:
            total = total+1
    # Chiffre en position impaire
    else:
        total = total + int(numero[i])
    i = i + 1

# Vérification que le total est un multiple de 10
if total%10 == 0:
    print("Numéro valide")
else:
    print("Numéro non valide")