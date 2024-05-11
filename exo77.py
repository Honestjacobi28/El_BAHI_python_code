'''
Ecrire un programme qui affiche la ou les solutions
d'une équation du second degré de la forme
ax2+bx+c. Utiliser une fonction pour calculer
le discriminant Delta et une autre pour afficher
les solutions delta.

PS: Pour calculer la racine carée d'un nombre, nous
utilisons la fonction :sqrt
Eg:Après l'éxécution de instruction suivante la valeur de 
A sera 2
    import math
    A=math.sqrt(4)
'''

from math import sqrt

def discrimant(a,b,c):
    delta=(b**2)-4*a*c
    return delta

def solutions(a,b,c):
    delta=discrimant(a,b,c)
    if delta<0:
        print("pas de solutions réelles")
    elif delta==0:
        x=(-b)/2*a
        print("La solution est : ",format(x,".2f"))
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("Les solutions sont : ",format(x1,".2f"),"et",format(x2,".2f"))

        
a=float(input("saisir la valeur de a: "))
b=float(input("saisir la valeur de b: "))
c=float(input("saisir la valeur de c: "))
solutions(a,b,c)