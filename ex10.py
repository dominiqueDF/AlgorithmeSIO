##
# Plus grand nombre parmi
# 10 saisis par l'utilisateur
#

for i in range(0,10):
    n = int(input("Saisir un nombre :"))
    if i==0:
        max = n
    elif n>max:
        max = n

print("Le maximum est ",max)