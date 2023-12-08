'''
   Exo 8 
   
   Ecrire un programme qui demande à l'utilisateur  de saisir deux entiers A et B ,
   qui échange le contenu des variables A et B puis qui affiche A et B

'''

A= int(input("donnez une valeur à A:"))
B= int(input("donnez une valeur à B:"))

'''
C=A
A=B
B=C
'''
# ou plus simplement uniquement en python
A,B=B,A
print('la nouvelle valeur de A est de :',A)
print(f'la nouvelle valeur de B est de :{B}')

