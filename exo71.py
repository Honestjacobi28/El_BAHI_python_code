'''
FONCTIONS ET MODULES

Ecrire  un programme utilisant une fonction qui affiche
le tableau de multiplication d'un entier positif x

'''

def table_multiplication(N):
    for i in range(1,11):
        print(i,"*",N,"=",i*N)
        

while True:
    N=int(input("Veuillez saisir un nombre: "))
    if N>0:
        break
table_multiplication(N)