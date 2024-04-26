'''
Ecrire un programme qui lit deux matrices
A et B de meme dimensions  4 et 5 et 
qui effecture l'addition des deux 
matrices. Le résultat de l'addition sera
affecté à la matrice C qui sera ensuite
affichée.
'''

A=[]
B=[]
C=[]

print('Veuillez saisir les éléments de la matrice A : ')

for i in range(4):
    ligne=[]
    for j in range(5):
        print('A[',i,'][',j,']= ',end=' ')
        ligne.append(int(input()))
    A.append(ligne)
    
print('Veuillez saisir les éléments de la matrice B : ')

for i in range(4):
    ligne=[]
    for j in range(5):
        print('B[',i,'][',j,']= ',end=' ')
        ligne.append(int(input()))
    B.append(ligne)
    
for ligneA,ligneB in zip(A,B):
    ligne=[]
    for eA,eB in zip(ligneA,ligneB):
        ligne.append(eA+eB)
    C.append(ligne)
    
print('La matrice A est :')
for ligne in A:
    for e in ligne:
        print(e,end='\t')
    print()
    
print('La matrice B est :')
for ligne in B:
    for e in ligne:
        print(e,end='\t')
    print()
    
print('Le resultat de addition de A et B est : ')
for ligne in C:
    for e in ligne:
        print(e,end='\t')
    print()