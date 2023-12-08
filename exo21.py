'''Ecrire un programme qui demande à utilisateur de 
   saisir un nombre puis en fonction du nombre saisi:
   -6:affiche "le personnage va à droite".  
   -4:affiche "le personnage va à gauche".  
   -8:affiche "le personnage va  en haut".  
   -2:affiche "le personnage va  en bas".  
   -dans le cas d'un autre caractere,
    affiche "erreur de saisie,
    le personnage ne bouge pas".  
'''

A=int(input("Entrez un nombre :"))

if A==6:
    print("le personnage va à droite")
elif A==4:
    print("le personnage va à gauche")
elif A==8:
    print("le personnage va en haut")
elif A==2:
    print("le personnage va en bas ")
else:
    print("erreur de saisie,le personnage ne bouge pas")
    