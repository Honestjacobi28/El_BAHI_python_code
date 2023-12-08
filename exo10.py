''' 
  Exo10
  
  Ecrire un programme qui calcule et affiche la distance entre deux points A et B
  du plan dont les coordonnées (Xa,Ya) et (xb,yb) sont entrées au clavier comme entiers.
  NB: utiliser la fonction math.sqrt pour calculer la racine carrée.
'''
import math

Xa=float(input("Entrez Xa: "))
Xb=float(input("Entrez Xb: "))
Ya=float(input("Entrez Ya: "))
Yb=float(input("Entrez Yb: "))

AB=(Xb-Xa)**2 + (Yb-Ya)**2
AB=math.sqrt(AB)

print("la distance AB est de:",format(AB,".2f"),"UA")