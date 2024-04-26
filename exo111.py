''' 
 Ecrire un programme qui demande à user
 de remplir deux listes (taille 6)
 puis le programme vérifie si les deux
 listes ont au moins un élément en commun ou non
'''

L=[]

for i in range(1,7):
    print('L[',i,']=',end=' ')
    L.append(float(input()))

N=[]
   
for i in range(1,7):
    print('N[',i,']=',end=' ')
    N.append(float(input()))

existe=False

for i in L:
    if i in N:
        existe=True
        break
if existe:
    print('L=',L, 'et ', 'N=',N , ' ont au moins un   élément en commun')
else: 
    print('L=',L, 'et ', 'N=',N , ' ont aucun   élément en commun')



