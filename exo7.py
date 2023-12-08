''' 
  Exercice 7
  
  Ecrire un programme qui demande à l'utilisateur de taper le rayon d'une sphere , puis calcule et affiche  son volume
  VS=4/3 piR3
'''

import math
rayon_sphere=float(input("quel est le rayon de la sphere :"))
VS=(4*math.pi*(rayon_sphere**3))/3

print("le volume de la sphere est :",format(VS,".2f"),"metre-cube")
