'''
Ecrire un programme qui demande à utilisateur 
d'entrer un entier,puis le programme utilise
une fonction pour compter et affiche le 
nombre de chiffres qui composent cet 
entier.  
'''

def compte(N):
    Nbr=0
    while N!=0:
        N=int(N/10)
        Nbr+=1
    return Nbr

N=int(input("Veuillez saisir un nombre: "))
print("Nombre total de chiffre dans le nombre ",N,"est: ",compte(N))