'''
Ecrire un programme qui calcule et affiche la somme,le produit
et la moyenne des éléments d'un tuple de 8 éléments
'''

T=(10,15,5,9,-9,2,7,1)
S=sum(T)
M=S/len(T)
P=1
for n in T:
    P=P*n
print('La somme des éléments du tuple est : ',S)
print('La moyenne des éléments du tuple est : ',M)
print('Le produit des éléments du tuple est : ',P)