"""
Ecrire un programme qui évalue les fonctions mathématiques 
suivantes:
f(x)=cos(4x)
f'(x)=-4sin(4x)
f''(x)=-16cos(4x)

calculer les résultats de x=0,x=pi/2,x=pi,x=-pi/2

"""

from math import cos,sin,pi

def f(x):
    y=cos(4*x)
    return y

def fd(x):
    y=-4*sin(4*x)
    return y
    
def fdd(x):
    y=-16*sin(4*x)
    return y
# x=0    
print(f(0))
print(fd(0))
print(fdd(0))

# x=pi/2
print(format(f(pi/2),".2f"))
print(format(fd(pi/2),".2f"))
print(format(fdd(pi/2),".2f"))


# x=pi
print(format(f(pi),".2f"))
print(format(fd(pi),".2f"))
print(format(fdd(pi),".2f"))

# x=-pi/2
print(format(f(-pi/2),".2f"))
print(format(fd(-pi/2),".2f"))
print(format(fdd(-pi/2),".2f"))
