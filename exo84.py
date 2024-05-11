'''
Ecrire un programme qui affiche le résultat de lancement d'un dé,
nous gagnons la partie si le numéro est 2 ou 5,sinon nous 
perdons la partie.
- ajoutez les instructions qui vous permettent de simuler 
ce jeu 10 fois , en affichant à chaque fois "gagné" 
ou "perdu".
- ajoutez les instructions pour compter combien de fois
nous gagnons si nous jetons le dé 1000 fois successives.
'''

from random import randint


for i in range(0,10):
    x=randint(1,10)
    if x==2 or x==5:
        print("vous avez gagné")
    else:

        print("vous avez perdu")
        
print("-----------------------------")        
nbr=0      
for i in range(0,1000):
    x=randint(1,10)
    if x==2 or x==5:
        nbr+=1
print("vous avez gagné",nbr,"fois en 1000 jets de dé successifs")
    