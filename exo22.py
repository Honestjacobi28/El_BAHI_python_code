'''
 Ecrire un programme qui vérifie si un nombre est pair ou impair
  
'''


A=int(input("veuillez entrer un entier: "))

if A%2==0:
    print(f"{A} est un nombre pair")
    # ou
    # print(A," est un nombre pair")
else:
    print(f"{A} est un nombre impair")
