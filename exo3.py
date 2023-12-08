

"""
 EXERCICE 3
  
 Ecrire un programme qui demande à l'utilisateur de taper la largeur et la longueur
 d'un rectangle et qui en affiche le perimetre et la surface. 
"""

largeur= float(input("quelle est la largeur ? : "))
longueur=float(input("quelle est la longueur ? : "))

perimetre=2*(largeur+longueur)
surface=largeur*longueur

# format(): donne le nbr de chiffre apès virgule
print("la valeur du perimetre est de :",format(perimetre,".2f"),"mètre") 
print("la valeur de la surface est de : ",format(surface,".2f"),"mètre-carré")