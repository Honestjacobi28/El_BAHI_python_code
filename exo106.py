''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis l'utilisateur est à nouveau invité à entrer 
 un entier n. l'objectif etant de vérifier 
 l'existence du nombre n dans L
'''

L=[]

for i in range(1,6):
    print('L[',i,']=',end=' ')
    L.append(int(input()))

n=int(input("saisir n : "))
if n in L:
    print(n,'se trouve dans la liste L= ',L)
else:
    print(n,'ne se trouve pas  dans la liste L= ',L)

        

