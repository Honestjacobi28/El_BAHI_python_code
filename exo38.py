'''
Ce jeu est tres simple. L'ordinateur tire un nombre
au hasard entre 1 et 30 et vous avez cinq essais pour 
le trouver. Apres chaque tentative,l'ordinateur
vous dira si le nombre que vous avez proposé est 
trop grand , trop petit , ou si vous avez 
trouvé le bon nombre 
'''

from random import randint

n=randint(1,30)
nombreTentative=5
while nombreTentative>0:
    nombreTentative-=1
    var=int(input("Entrer un nombre entre 1 et 30 : "))
    if var < n:
        print("C'est plus !")
    elif var>n:
        print("C'est moins !")
    else:
        break
    
if nombreTentative !=0:
    print("Bravo vous avez trouvé",var,"en",5-nombreTentative,"essais")
else:
    print("Oups! vous avez depassé les 5 tentatives autorisées. Le nombre etait:",n)
    