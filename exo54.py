'''
Ecrire un programme permettant de prendre un nombre C
de colonnes 
puis de réaliser la forme suivante(C=4):

        * 
        * * 
        * * * 
        * * * * 
        * * * 
        * * 
        * 
'''

C=int(input("Saisir le nombre de colonnes: "))
P=1
for i in range(1,C*2-1+1):
    for j in range(1,P+1):
        print("* ",end="")
    if i<C:
        P+=1
    else:
        P-=1    
    
    print()
    
    
