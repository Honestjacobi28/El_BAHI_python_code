''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis l'utilisateur est à nouveau invité à entrer 
 un entier n. l'objectif etant de calculer  
 le nombre d'occurence de n dans L
'''

L=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(int(input()))

n=int(input("saisir n : "))
occ=L.count(n)
print('Le nombre occurence de','n,dans L=',L, 'est : ',occ)


        

