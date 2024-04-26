''' 
 Ecrire un programme qui demande à user
 d'entrer une phrase et une lettre.
 Ensuite, le programme compte l'ocurrence 
 de la lettre dans la phrase 
'''

phrase=input("Veuillez saisir une phrase : ")
lettre=input("Veuillez saisir une lettre : ")

P=list(phrase)
n=P.count(lettre)
print("Le nombre occurrence de",lettre, "dans la phrase est : ",n)
print(P)


