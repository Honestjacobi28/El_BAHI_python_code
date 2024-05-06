'''
Ecrire un programme qui demande à utilisateur
d'entrer un entier, puis le programme compte
et affiche le nombre de chiffres qui 
compose cet entier
'''

N= int(input("Saisir la valeur de  N: "))
M=N
nbr=0
while N !=0:
    N=N//10
    nbr+=1
print("Nombre total de chiffres est dans le nombre",M,"est: ",nbr)