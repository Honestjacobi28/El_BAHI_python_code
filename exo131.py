'''
Ecrire un programme qui demande à utilisateur
d'entrer n entiers stockés dans une liste L
Puis le programme détermine et affiche les
éléments nobles de la liste
NB:un élément x est dit noble dans 
une liste si le nombre d'éléments
supérieurs à x est égal à x
'''

n=int(input("saisir la la taille de la liste: "))
L=[]
for i in range(n):
    print('L[',i+1,']= ',end=' ')
    L.append(int(input()))


for i in L:
    nbr=0
    for j in L:
        if(i<j):
            nbr+=1
    if(nbr==i):
            print(L)
            print(i,'est un nombre noble')
            
            