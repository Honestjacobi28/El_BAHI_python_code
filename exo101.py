'''
Ecrire un programme qui effectue le produit 
scalaire  de deux  vecteurs de mm taille
(3 éléments) représentés par des liste à 
une dimention
'''

U=[]
V=[]

for i in range(1,4):
   print('U[',i,']=',end=' ')
   U.append(float(input()))
   print('V[',i,']=',end=' ')
   V.append(float(input()))
   
# méthode 1:

#p = U[0]*V[0] + U[1]*V[1] + U[2]*V[2]


# méthode 2:
p=0
for Ue,Ve in zip(U,V):
    p+= Ue*Ve
    
print(p)

