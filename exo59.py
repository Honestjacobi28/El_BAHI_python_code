'''
Ecrire un programme permettant de prendre un nombre L
de lignes ,puis de réaliser
le triangle des nombres suivants (L=4)


        1 
        2 2 
        3 3 3 
        4 4 4 4
'''


L=int(input("veuillez saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()