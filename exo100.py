'''
Ecrire un programme à utilisateur de saisir
10 réels stockés dans une liste, puis le 
programme calcule et affiche la somme,
le produit et la moyenne des éléments
de la liste. 
'''

L=[]

for i in range(5): #10
    print('L[',i+1,']=',end=' ')
    L.append(float(input()))
print(L)
S=sum(L)
M=S/len(L)
P=1

for n in L:
    P*=n

print('La somme des éléments de la liste est : ',S)
print('La moyenne des éléments de la liste est : ',M)
print('Le produit des éléments de la liste est : ',P)