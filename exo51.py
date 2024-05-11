'''
Ecrire un programme permettant de prendre un nombre L
de lignes 
puis de réaliser un "losange d'étoiles". de la longueur L 
dans chaque coté.
'''

L=int(input("Saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,L-i+1):
            print("  ",end="")
    for j in range(1,L+1):
            print("* ",end="")
    print()