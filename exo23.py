'''
 Ecrire un programme qui demande à l'utilisateur 
 de saisir une année et vérifie si elle est 
 bissextile(366 jours) ou non 
'''


A=int(input("veuillez entrer une année: "))

if ((A%4==0 and A%100!=0) or (A%400==0)): 
    print(A," est une annee bissextile")
else:
    print(f"{A} est un annee non bissextile")
