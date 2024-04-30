'''
Ecrire un programme qui demande au joueur 
de selectionner 6 numéros différents
entre 1 et 49. Ensuite, le programme simule
une série de tirages automatiques. A chaque 
tirage, 6 numéros différents entre 1 et 49 sont
générés automatiquement .Le but  du programme est 
de déterminer après combien de tirages le joueur
gagnera au loto et combien d'argent perdra.

NB:Pour jouer une grille loto simple, le joueur dois miser
2,20€
'''

import random 

def selection():
    joueurNums=[]
    for i in range(0,6):
        num=int(input('Veuillez saisir un nombre entre 1 et 49 : '))
        while(num in joueurNums or num<1 or num>9):
            num=int(input('Veuillez saisir un nombre entre 1 et 49 : '))
        joueurNums.append(num)
    joueurNums.sort()
    return joueurNums


def tirageDuJour():
    tirage=[]
    for i in range(0,6):
        num=random.randint(1,9)
        while(num in joueurNums):
            num=random.randint(1,9)
        tirage.append(num)
    tirage.sort()
    return tirage


joueurNums=selection()  
cmp=0
while True:
    tirage=tirageDuJour 
    cmp+=1
    print(cmp)
    if joueurNums==tirage:
        break      
    
    
print("Vous gagnerez au loto après :",cmp,"jours")
print("Vous perderez une somme de : ",cmp+2.2,"Euros")
print("votre selection : ",joueurNums)
print("les numeros de loterie sont : ",tirage)