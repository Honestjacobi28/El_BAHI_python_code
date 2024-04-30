'''
Ecrire un programme qui remplit une liste de deux
dimensions (4,6), puis le programme détermine:
- Le minimum et le maximum de chaque ligne.
- Le minimum et le maximum de chaque colonne
'''

M=[
    [2,3,5,7,0,9],
    [9,7,1,3,4,1],
    [5,6,5,8,7,4], 
    [9,5,4,3,8,3] ]

for ligne in M:
    for e in ligne:
        print(e,end='\t')
    print()
    
for i,ligne in enumerate(M,start=1):
    print("Le maximum de la ligne ",i,"est :",max(ligne))
    print("Le minimum de la ligne ",i,"est :",min(ligne))
    
    
for j in range(len(M[0])):
    minC=M[0][j]
    maxC=M[0][j]
    for i in range(1,len(M)):
        if minC >M[i][j]:
            minC=M[i][j]
        if maxC <M[i][j]:
            maxC=M[i][j]
    print("Le maximum de la colonne ",j+1,"est : ",maxC)
    print("Le minimum de la colonne ",j+1,"est : ",minC)