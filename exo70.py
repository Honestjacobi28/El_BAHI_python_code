'''
Ecrire un progamme permettant de prendre un nombre L de lignes,
puis de réaliser le triangle des alphabets de Tifinagh suivant
(L=4)

      ⵖ 
    ⵗ ⵘ ⵙ 
  ⵚ ⵛ ⵜ ⵝ ⵞ 
ⵟ ⵠ ⵡ ⵢ ⵣ ⵤ ⵥ 

'''

L=int(input("Veuillez saisir le nombre de lignes: "))
n=11606
for i in range(1,L+1):
    for j in range(1,L-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(chr(n),end=" ")
        n+=1
    print()
