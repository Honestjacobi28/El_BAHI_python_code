'''
Ecrire un programme qui remplit une matrice(liste à 2D).
Puis le programme échange les éléments du triangle
inférieur avec le triangle supérieur de la matrice
'''

# Produit de matrice

'''
Ecrire un programme qui remplit une liste de 
deux dimensions et de meme taille(4,4) 
puis le programme calcule la somme de
la diagonal principale.
'''

M=[
    [2,3,5,7,9],
    [0,9,3,9,7],
    [7,1,3,4,1], 
    [9,0,8,2,4] ]

print("la matrice initiale: ")
for ligne in M:
    for e in ligne:
         print(e,end='\t')
    print()
    
for i in range(len(M)-1):
    for j in range(i,len(M)):
        temp=M[i][j]
        M[i][j]=M[j][i]
        M[j][i]=temp

print("la matrice après échange: ")

for ligne in M:
    for e in ligne:
        print(e,end='\t')
    print()