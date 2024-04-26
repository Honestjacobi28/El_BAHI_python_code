''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis le programme  détermine et affiche 
 le deuxième plus grand nombre des de la liste.
'''

L=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(int(input()))

L.sort(reverse=True)   
print(L)
print("Le deuxième plus grand nombre de la liste est: ",L[1])