"""
Creer une fonction qui prend x comme argument et renvoie y.
y est calculer à aide f(x)=4x3 -13x2 + x -60
"""

def f(x):
    y=4*(x**3)-13*(x**2)+x-60
    return y


x=int(input("veuillez saisir la valeur de x: "))
y=f(x)
print("f(",x,")=",y)