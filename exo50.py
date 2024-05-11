'''
Ecrire un programme permettant à utilisateur d'entrer la 
longueur d'un coté L (impaire) d'un carré   
puis de le programme dessine la forme suivante
(L=5)
'''

L=int(input("Saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,L+1):
        if i==1 or i==L or j==1 or j==L or i==j or j==L-i+1:
            print("* ",end="")
        else:
            print("  ",end="")
    
    print()