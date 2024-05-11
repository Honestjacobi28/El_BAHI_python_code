'''
Ecrire un programme permettant de prendre un nombre L
de lignes et un nombre C de colonnes
puis de réaliser un "cadre étoile". de L lignes
par C colonnes
'''

L=int(input("Saisir le nombre de lignes: "))
C=int(input("Saisir le nombre de colonnes: "))
for i in range(1,L+1):
    for j in range(1,C+1):
        if i==1 or i==L or j==1 or j==C:
            print("* ",end="")
        else:
            print("  ",end="")
    
    print()