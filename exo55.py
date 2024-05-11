'''
Ecrire un programme permettant de prendre un nombre L
de lignes 
puis de réaliser le diamant suivant(L=4):

       * * 
    * * * * 
  * * * * * * 
* * * * * * * * 
  * * * * * * 
    * * * * 
      * * 
'''

L=int(input("Saisir le nombre de lignes: "))
espace=L-1
etoile=1
for i in range(1,L*2):
    for j in range(0,espace):
        print("  ",end="")
    for j in range(0,etoile*2):
        print("* ",end="")
    if i<L:
        espace-=1
        etoile+=1
    else:
        espace+=1
        etoile-=1
   
    # passer à la ligne suivante ,end reste dans la memoire
    print()
    
# pas de *  dans le diamant
