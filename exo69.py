'''
Ecrire un  programme permettant de prendre un nombre  L
de lignes,puis de réaliser le triangle des alphabets
suivant (L=4) :
      A 
    B C 
  D E F 
G H I J 
'''
L=int(input("Veuillez saisir le nombre de lignes: "))
n=65
for i in range(1,L+1):
    for j in range(1,L-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n+=1
    print()


