'''
Ecrire un programme qui vérifie
si une matrice donnée est creuse 
ou non.

NB:une matrice est creuse si la plupart
de ses éléments sont des zéros 
'''

M=[
    [1,0,3,0],
    [0,0,4,1],
    [6,0,0,0]
]

nbr=0

for ligne in M:
    for ele in ligne:
        if ele==0:
            nbr+=1
            
l=len(M)
c=len(M[0])
if nbr>l*c//2:
    print('La matrice est creuse')
else:
    print('La matrice est pas creuse')
            