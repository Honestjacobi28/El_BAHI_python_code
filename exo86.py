"""
Nous considérons la fonction ci-contre.
Quel est les résultats des appels suivants :

f(0,0,0)
f(-4,-1)
f(-1,9,5)
f(c=-1,b=9,a=5)
f(-2,3,0)
f(2,0,2)
f(1,0,2)
f(b=-2,c=0,a=3)
f(8,2)
f(3,-1,-2)
"""

def f(a,b,c=1):
    if a>b:
        a,b=b,a
    if a>c:
        return a
    elif c>=b:
        return b
    else:
        if (a-c)>(b-c):
            return b
        else:
            return a
        
print(f(0,0,0))
print(f(-4,-1))
print(f(-1,9,5))
print(f(c=-1,b=9,a=5))
print(f(-2,3,0))
print(f(2,0,2))
print(f(1,0,2))
print(f(b=-2,c=0,a=3))
print(f(8,2))
print(f(3,-1,-2))





