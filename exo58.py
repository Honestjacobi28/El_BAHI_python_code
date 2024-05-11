'''
Ecrire un programme permettant de prendre un nombre L
de lignes et nombre C de colonnes,puis de réaliser
le rectangle des nombres suivant (L=4,C=7)


       1 1 1 1 1 1 1 1
       2 2 2 2 2 2 2 2
       3 3 3 3 3 3 3 3
       4 4 4 4 4 4 4 4
'''


L=int(input("veuillez saisir le nombre de lignes: "))
C=int(input("veuillez saisir le nombre de colonnes: "))
for i in range(1,L+1):
    for j in range(1,C+1):
        print(i  ,end=" ")
    print()