'''
  Créer un programme qui permet d'automatiser le jeu
  Pierre, Feuille, Ciseaux.
'''

import random

nom=input("Veuillez saisir votre nom :")
user_victoires=0
pc_victoire=0
nuls=0


while True:
     print(nom," : ",user_victoires,"égalité : ",nuls," PC : ",pc_victoire)
     coupJoueur = input("Entrer votre coup: (p)ierre,(f)euille,(c)iseaux ou (q)uitter:")
     if coupJoueur=="q":
         break
     if coupJoueur != "p" and coupJoueur!="f" and coupJoueur!="c":
         continue
     
     
     if coupJoueur=="p":
         print("PIERRE contre ...",end=" ")
         
     elif coupJoueur=="f":
        print("FEUILLE contre ...",end=" ")
     else:
        print("CISEAUX contre ...",end=" ")
        
        
     randomNombre=random.randint(1,3)
     if randomNombre==1:
         coupPC="p"
         print("PIERRE")
     elif randomNombre==2:
        coupPC="f"
        print("FEUILLE")
     else:
        coupPC="c"
        print("CISEAUX")
        
     if  coupJoueur== coupPC:
         print("Partie est nulle ! ")
         nuls+=1
     elif coupJoueur=="p" and coupPC == "c" :
         print("Vous avez gagné !")
         user_victoires+=1
     elif coupJoueur=="f" and coupPC == "p" :
         print("Vous avez gagné !")
         user_victoires+=1
     elif coupJoueur=="c" and coupPC == "f" :
         print("Vous avez gagné !")
         user_victoires+=1
     elif coupJoueur=="p" and coupPC == "f" :
         print("Vous avez perdu !")
         pc_victoire+=1
     elif coupJoueur=="f" and coupPC == "c" :
         print("Vous avez perdu !")
         pc_victoire+=1
     elif coupJoueur=="c" and coupPC == "p" :
         print("Vous avez perdu !")
         pc_victoire+=1
     
         
          
        
         