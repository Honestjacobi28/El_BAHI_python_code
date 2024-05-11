'''
Ecrire un programme qui demande à User d'entrer un nombre L
de lignes. Ensuite,le programme basé sur une fonction
dessine le triangle suivant(L=5):


        * 
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * *
'''
def triangle(L):
    for i in range(1,L+1):
        for j in range(1,L-i+1):
                print("  ",end="")
        for j in range(1,2*i-1+1):
                print("* ",end="")
        print()
    
L=int(input("Saisir le nombre de lignes: "))
triangle(L)
    
# pas de ** etoiles
