''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis le programme  détermine et affiche 
 les éléments uniques de la liste.
'''

L=[]
U=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(int(input()))
    
for i in L:
    if L.count(i)==1:
        U.append(i)
        
print(L)
print("Les éléments uniques de la liste sont: ",U)

    
