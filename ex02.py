##
# Calcul de la moyenne de deux notes
# comprises entre 0 et 20
#

note1 = -1
while note1<0 or note1>20:
    note1 = int(input("Saisir la 1ère note:"))
note2 = -1
while note2<0 or note2>20:
    note2 = int(input("Saisir la 2ème note:"))
moyenne = (note1+note2)/2
print("La moyenne est ", moyenne)