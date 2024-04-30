'''
Ecrire un programme qui demande à 
utilisateur d'entrer un nombre 
positif n, puis le programme crée
une matrice identité de taille 
(n*n).
NB:Une matrice identité ou  matrice unité
est une matrice carrée avec des 1 sur 
la diagonale et des 0 partout ailleurs.

'''

n= int(input('Veuillez saisir la taille de la liste : ' ))
M=[]
for i in range(n):
    ligne=[]
    for j in range(n):
       if (i==j):
           ligne.append(1)
       else:
           ligne.append(0)
    M.append(ligne)
    
for ligne in M:
    for e in ligne:
        print(e,end='\t')
    print()
        