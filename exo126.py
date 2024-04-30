'''
Ecrire un programme 
qui permet de construire le triangle de PASCAL de 
dégré n
'''

while True:
    n=int(input("Veuillez entrer le nombre de lignes : "))
    if n>1:
        break
    
P=[]
for i in range(n):
    ligne=[]
    ligne.append(1)
    for j in range(1,i):
        ligne.append(P[i-1][j-1]+P[i-1][j])
    if(i!=0):
       ligne.append(1)
    P.append(ligne)
    

for ligne in P:
    for e in ligne:
        print(e,end='\t')
    print()