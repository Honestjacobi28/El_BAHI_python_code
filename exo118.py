
'''
Ecrire un programme qui permet de déclarer
une liste de deux dimentions(3,6),puis le 
programme remplit la liste avec des valeurs
nulles.

'''

M=[]

for i in range(3):
    ligne=[]
    for j in range(6):
        ligne.append(0)
    M.append(ligne)

# affiche matrice   
for l in M:
  print(l)