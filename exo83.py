"""
En important uniquement les fonctions nécessaires du module 
math, ecrivez deux fonctions pour vérifier la validité de 
la formule suivante pour n=10:

sigma i=0 à n cos(ix)=1/2 + sin((2n+1/2)x)/2sin(1/2x)
"""

from math import cos,sin

def p1(x):
    S=0
    for i in range(0,11):
        S=S+cos(i*x)
    return S

def p2(x):
    R=1/2 + (sin(((2*10+1)/2)*x))/(2*sin(x/2))
    return R

x=int(input("veuillez saisir une valeur de x: "))
S=p1(x)
R=p2(x)
print(format(S,".2f"))
print(format(R,".2f"))
