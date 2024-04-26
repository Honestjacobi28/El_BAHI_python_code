''' 
 Ecrire un programme permettant , à utilisateur
 de saisir les notes d'une classe(10 étudiants).
 le programme , une fois la saisie terminée,
 renvoie le nombre de ces notes supérieures
 à la moyenne de la classe
'''

L=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(float(input()))

m=sum(L)/len(L)
nbr=0
for n in L:
    if n>=m:
        nbr+=1
print('la moyenne de la classe est de : ',m)
print('Le nombre de notes supérieurs à la moyenne est : ',nbr)

