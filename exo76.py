'''
Ecrire un programme utilisant des fonctions 
qui demande à utilisateur de saisir le 
rayon du cercle, puis le programme affiche
le diamètre ,la surface et le périmetre 
du cercle 
'''

import math
 
def diametre(R):
    print("Le diamètre du cercle est : ",R*2) 
    
def surface(R):
    print("La surface du cercle est : ",format(math.pi*(R**2),".2f")) 
    
def perimetre(R):
    print("Le perimetre du cercle est : ",format(2*math.pi*R,".2f")) 
    

R=int(input("Veuillez entrer le rayon du cercle :"))
diametre(R)
surface(R)
perimetre(R)