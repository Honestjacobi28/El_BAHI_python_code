'''
Ecrire un programme qui demande à utilisateur
d'entrer n(n>2) nombres stockés dans une liste
L. 
NB: Un élément d'une liste est un pic s'il est
supérieur à ses voisins. Pour le premier et 
le dernier élément de la liste, nous devons 
considérer un seul voisin.
'''

n=int(input("saisir la la taille de la liste: "))
while n<3:
    n=int(input("saisir la la taille de la liste: "))
    
L=[]
for i in range(n):
    print('L[',i,']= ',end=' ')
    L.append(int(input()))
    
print('Les pics de la liste sont : ')
if(L[0]>L[1]):
    print(L[0])
if (L[n-1]>L[n-2]):
    print(L[n-1])
for i in range(1,n-1):
    if(L[i]>L[i-1] and L[i]>L[i+1]):
        print(L[i])
