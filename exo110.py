''' 
 Ecrire un programme qu renverse une liste(taille)
 sans utiliser la méthode reverse. Celui-ci doit
 prendre comme entrée une liste et renvoyer la 
 liste de meme taille ayant les valeurs
 dans l'ordre inverse.
'''

L=[]
T=[]

for i in range(1,7):
    print('L[',i,']=',end=' ')
    L.append(float(input()))
    
for i in range(5,-1,-1):
    T.append(L[i])


print('la liste initiale  : ',L)
print('la liste inversée : ',T)

