from stats87 import *


N1=float(input("saisir la note 1: "))
N2=float(input("saisir la note 2: "))
N3=float(input("saisir la note 3: "))
N4=float(input("saisir la note 4: "))
N5=float(input("saisir la note 5: "))

S=somme(N1,N2,N3,N4,N5)
M=moyenne(N1,N2,N3,N4,N5)
V=variance(N1,N2,N3,N4,N5)
E=ecart_type(N1,N2,N3,N4,N5)
CV=coefficient_variation(N1,N2,N3,N4,N5)

print("la somme des notes est: ",S)
print("la moyenne des notes est: ",M)
print("la variance des notes est: ",V)
print("l'ecart-type des notes est: ",E)
print("le coefficient de variation des notes est: ",CV)


