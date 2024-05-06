'''
Ecrire un programme qui utilise un menu pouvant 
effectuer les opérations suivantes: somme,soustraction
multiplication,division,le reste d'une division 
entière et puissance.
Après avoir choisir  opération , le programme doit
demander à utilisateur d'entrer les deux termes 
de l'opération,puis le programme affiche le
résultat.
Le programme doit également demander à utilisateur
s'il souhaite démarrer une autre opération
ou quitter le programme.
'''

while True:
    print("-------Calculatrice: MENU-------")
    print("1- Addition.")
    print("2- Soustraction.")
    print("3- Multiplication.")
    print("4- Division.")
    print("5- Reste d'une division entière.")
    print("6- Puissance.")
    operation=int(input("Quel calcul veux-tu effectuer: "))
    A=int(input("saisir le premier terme: "))
    B=int(input("saisir le deuxieme terme: "))
    if operation==1:
        print("Le résultat est : ",A+B)
    elif operation==2:
        print("Le résultat est : ",A-B)
    elif operation==3:
        print("Le résultat est : ",A*B)
    
    elif operation==4:
        if B!=0:
           print("Le résultat est : ",A/B)
        else:
            print("La division par 0 est impossible")
    elif operation==5:
        if B!=0:
           print("Le résultat est : ",A%B)
        else:
            print("La division par 0 est impossible")
    elif operation==6:
        print("Le résultat est : ",A**B)
        
    else:
        print("Le résultat est incorrect")
    reponse=input("Veux-tu faire un autre calcul (O/N) :  ")
    if reponse=="N":
        break
        
    