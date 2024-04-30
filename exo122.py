# Produit de matrice

'''
Ecrire un programme qui remplit une liste de 
deux dimensions et de meme taille(4,4) 
puis le programme calcule la somme de
la diagonal principale.
'''

M=[
    [2,3,5,7],
    [0,9,3,7],
    [7,1,3,4], 
    [9,0,8,2] ]

S=0

for i in range(4):
    for j in range(4):
         if (i==j):
             S+=M[i][j]

print('La somme de la diagonal principale de la matrice M est: ',S)