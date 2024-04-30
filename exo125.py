'''
Ecrire un programme qui demande à utilisateur
de remplir une liste de deux dimensions T
de taille (2,2).Ensuite le programme calcule
et affiche le déterminant de matrice
'''

T=[]
print("Saisir les éléments de la matrice T : ")

for i in range(2):
    ligne=[]
    for j in range(2):
        print('T[',i+1,'][',j+1,']= ',end=' ')
        ligne.append(int(input()))
    T.append(ligne)
    
det=T[0][0]*T[1][1]-T[0][1]*T[1][0]

print('La matrice T est :')

for ligne in T:
    for e in ligne:
        print(e,end='\t')
    print()
    
print("le determinant de la matrice  T est : ",det)