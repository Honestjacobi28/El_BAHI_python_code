''' 
Ecrire un programme qui demande à utilisateur d'entrer 
un caractère et vérifie si le caractère donné est un
alphabet,un nombre ou un caractère spécial
'''

# mes recherches
'''A=(input("Entrez un caractère:"))

if A.isalpha():
    print(A,"est un alphabet")
elif A.isdigit():
    print(A,"est un un nombre")
    
else:
    print(A,"est un un caractère spéciale")
'''

# solutions

caractere=input("Entrez un caractère: ")

if ("A"<=caractere and "Z">=caractere) or ("a"<=caractere and "z">=caractere):
    print(caractere,"est un alphabet")
    
elif ("1"<=caractere and "9">=caractere):
    print(caractere,"est un un nombre")
    
else:
    print(caractere,"est un un caractère spéciale")
    
    