'''
Ecrire un  programme permettant de prendre un nombre  L
de lignes,puis de réaliser le triangle des alphabets
suivant (L=5) :

A
B C
D E F
G H I J
K L M N O

'''
L=int(input("Veuillez saisir le nombre de lignes: "))
n=65
for i in range(1,L+1):
    for j in range(i):
        print(chr(n),end=" ")
        n+=1
    print()


