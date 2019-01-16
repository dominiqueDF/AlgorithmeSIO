##
# Plus grand nombre parmi
# ceux saisis par l'utilisateur
#

n = int(input("Saisir un nombre :"))
max = n
while n!=0:
    n = int(input("Saisir un nombre :"))
    if n>max:
        max = n

print("Le maximum est ",max)