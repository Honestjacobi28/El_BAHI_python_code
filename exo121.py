# Produit de matrice

'''
Ecrire un programme qui lit deux matrices
A(3,4) et B(4,2) et 
qui effecture le produit des deux 
matrices. 
'''

A=[
    [2,3,5,7],
    [0,9,3,7],
    [7,1,3,4] ]
  
B=[
    [5,6],
    [4,7],
    [2,0],
    [0,1] ]

C=[
    [0,0],
    [0,0],
    [0,0] ]


for i in range(len(A)):
    for j in range(len(B[0])):
         for k in range(len(B)):
             C[i][j]+=A[i][k]*B[k][j]

print("A= ")
for ligne in A:
    for e in ligne:
        print(e,end='\t')
    print()
    
print("B= ")
for ligne in B:
    for e in ligne:
        print(e,end='\t')
    print()
    
print("A*B= ")
for ligne in C:
    for e in ligne:
        print(e,end='\t')
    print()
    