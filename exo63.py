'''
Ecrire un programme permettant de prendre un nombre L
de lignes ,puis de réaliser
la forme de nombres suivants (L=4)

1             1 
1 2         2 1 
1 2 3     3 2 1
1 2 3 4 4 3 2 1
'''


L=int(input("veuillez saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,L*2-i*2+1):
        print("  ",end="")
    for j in range(1,i+1):
        print(i-j+1,end=" ")
    print()