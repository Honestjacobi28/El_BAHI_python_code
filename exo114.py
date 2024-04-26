'''
Ecrire un programme qui contient deux fonctions:
- La première demande à utilisateur d'entrer n 
nombres stockés dans une liste L,
- La deuxième supprime les  nombres de la liste qui 
sont divisibles sur 5
liste.
'''


def remplissage():
    n=int(input('Entrer la taille de la liste : '))
    L=[]
    for i in range(n):
        print('L[',i,']=',end=' ')
        L.append(int(input()))
    return L

def suppression(L):
    for i in list(L):
        if i%5==0:
            L.remove(i)
    return L

L=remplissage()
L=suppression(L)
print(L)