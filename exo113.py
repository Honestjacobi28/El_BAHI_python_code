'''
Ecrire un programme qui contient deux fonctions:
- La première demande à utilisateur d'entrer n 
nombres stockés dans une liste L,
- La deuxième affiche les m(m<n) plus grands nombres de la 
liste.
'''


def remplissage():
    n=int(input('Entrer la taille de la liste : '))
    L=[]
    for i in range(n):
        print('L[',i,']=',end=' ')
        L.append(int(input()))
    return L

def m_max_elements(L):
    m=int(input('Entrer la valeur de m : '))
    L.sort()
    return L[-m:]

L=remplissage()
Max=m_max_elements(L)
print("les m plus grands éléments de la liste sont: ",Max)