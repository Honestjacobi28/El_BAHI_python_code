
'''
 Ecrire  un programme qui lit une matrice A(liste à 2 dimensions)
 de dimensions 4 et 6 au clavier et affiche a clavier
 et affiche les données suivantes:

 - La matrice A
 - La transposée de A
'''

A=[]
T=[]

print("Veuillez saisir les éléments de la matrice A : \n")

for i in range(4):
    ligne=[]
    for j in range(6):
        print('A[',i,'][',j,']= ',end=' ')
        ligne.append(int(input()))
    A.append(ligne)
    
for j in range(6):
    ligne=[]
    for i in range(4):
        ligne.append(A[i][j])
    T.append(ligne)
        
print('La matrice A est de : ')

for l in A:
    for e in l:
        print(e,end='\t1')
    print()
    
print('La matrice Transposée est de : ')

for l in T:
    for e in l:
        print(e,end='\t')
    print()