##
# Extraction de données d'un fichier texte
# et génération d'un nouveau fichier
#

import random
random.seed()

# Ouverture des fichiers (en lecture "r" et en écriture "w")
fichierIn = open("C:\\Users\\domin\\Documents\\emails.txt", "r")
fichierOut = open("C:\\Users\\domin\\Documents\\identifiants.txt", "w")

# Parcours du fichier d'emails tant qu'on peut en lire
email = fichierIn.readline()
while email:
    # Découpage de l'identifiant (partie précédent le symbole @)
    id = email[:email.find("@")]
    # Calcul d'un mot de passe
    password = ""
    for i in range(5):
        password += chr(random.randint(ord('A'),ord('z')))
    # Ecriture dans le fichier
    fichierOut.write(id+" "+password+"\n")
    # Lecture de l'email suivant
    email = fichierIn.readline()

# Fermeture des fichiers et "vidage" dutampon de celui en écriture
fichierIn.close() 
fichierOut.flush()
fichierOut.close()

