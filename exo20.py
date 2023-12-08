# EXERCICE

"""
Ecrire un programme qui demande deux nombres entiers et l'un 
des opérateurs suivant:+,-,*, / puis effectue l'opération
correspondant et affiche le résultat de cette opération. 
"""

A=int(input("Entrez un nombre entier: "))
op=(input("Entrez un opérateur( + - * /) : "))
B=int(input("Entrez un nombre entier: "))

if op=="+":
    print(f"{A}+{B} =",A+B)
elif  op=="-":
    print(f"{A}-{B} =",A-B)
elif  op=="*":
    print(f"{A}*{B} =",A*B)

elif  op=="/":
    if B!=0:
        print(f"{A}/{B} =",A/B)
    else:
        print("la division par zéro est impossible")

else:
    print("cet opérateur n'existe pas")




