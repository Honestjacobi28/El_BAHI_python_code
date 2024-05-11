'''
Ecrire un programme permettant de prendre un nombre L
de lignes,puis de réaliser un "triangle étoile".
'''

L=int(input("Saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(i):
        print("* ",end="")
    print()