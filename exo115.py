''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer n(n>2) nombres stockés dans une liste L,
 ensuite , le programme remplace chaque élément de
 la liste par la somme des deux éléments
 consécutifs suivant de manière circulaire
'''
n=int(input("veuillez saisir la taille de la liste :"))

while n<3:
    n=int(input("veuillez saisir la taille de la liste :"))
    
L=[]

for i in range(n):
    print('L[',i,']=',end=' ')
    L.append(int(input()))

e1=L[0]
e2=L[1]
for i in range(n-2):
    L[i]=L[i+1]+L[i+2]
    
L[n-2]=L[n-1]+e1
L[n-1]=e1+e2
print('les éléments de la liste après échange circulaire sont : ',L)


        

