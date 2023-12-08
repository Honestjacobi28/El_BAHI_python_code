# EXERCICE

""""
 Ecrire un programme qui affiche la ou les solutions d'une équation du second 
 degré de la forme ax2+bx+c
 NB:Utiliser la fonction sqrt() de la biblotheque math pour calculer la racine 
 carrée.
"""
from math import sqrt

a=float(input('valeur de a:'))
b=float(input('valeur de b:'))
c=float(input('valeur de c:'))

discriminant= b**2 - 4*a*c


if discriminant>0:
    x1=(-b-sqrt(discriminant))/(2*a)
    x2=(-b+sqrt(discriminant))/(2*a)
    # print(f"les solutions sont:{x1} ou {x2}")
    print("les solutions sont : ",format(x1,".2f"), "ou",format(x2,".2f"))
elif discriminant==0:
    x0=-b/(2*a)
    print(f"la solution est:{xO}")
else:
    print("pas de solution dans R")
    

