'''
Ecrire un programme qui demande à Utilisateur de saisir
une chaine de caractères, puis affiche cette chaine
sous forme de triangle.  
Eg avec le mot "hello"

h
he
hel
hell
hello
'''


mot=input("veuillez saisir un mot: ")
P=""
for i in mot:
    P+=i
    print(P)