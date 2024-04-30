'''
Ecrire un programme qui crée une liste contenant
le résultat de 1 000 000 d'expériences de pile
ou face générées aléatoirement. Ensuite, le programme
calcule le nombre de fois qu'une série de six piles ou
une série de six faces apparait d'affilée dans la liste.
NP : Utiliser random.choice(['P';'F']) pour 
générer aléatoirement soit P ou F.
'''


import random
nbrSeries=0
L=[]
F=['F']*6
P=['P']*6
# print(F)
# print(P)

for e in range(10000):
    r=random.choice(['P','F'])
    L.append(r)
    if e>=6:
        if L[-6:]==F or L[-6:]==P:
            print(L[-6:])
            nbrSeries+=1
print('la chance est ',(nbrSeries/10000),'%')
print(nbrSeries)
