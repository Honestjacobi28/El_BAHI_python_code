'''
Ecrire un programme permettant de prendre un nombre L
de lignes ,puis de réaliser
le triangle des nombres(0,1) suivants (L=4)


        1 
        1 0 
        1 0 1 
        1 0 1 0 
'''


L=int(input("veuillez saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,i+1):
        n=j%2
        print(n,end=" ")
    print()