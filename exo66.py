'''
Ecrire un programme permettant de prendre un nombre de L
de lignes,puis de réaliser le triangle de la lettre A
suivant(L=4)

A
A A
A A A
A A A A

'''
L=int(input("Veuillez saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,i+1):
        # lettre A
        C=chr(65)
        print(C,end=" ")
    print()

