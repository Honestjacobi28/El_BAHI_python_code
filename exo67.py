'''
Ecrire un  programme permettant de prendre un nombre  L
de lignes,puis de réaliser le triangle des alphabets
suivant (L=5) :

A
A B
A B C
A B C D
A B C D E

'''
L=int(input("Veuillez saisir le nombre de lignes: "))
for i in range(1,L+1):
    n=65
    for j in range(i):
        print(chr(n),end=" ")
        n+=1
    print()


