''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis le programme  détermine et affiche 
 les nombres pairs  de la liste.
'''

L=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(int(input()))

p=[]
for i in L:
    if i%2==0:
        p.append(i)
print(p)
print("Les nombres pairs de la liste sont: ",p)