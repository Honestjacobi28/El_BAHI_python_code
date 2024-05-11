'''
Ecrire un progamme qui demande à utilisateur d'entrer 
un en entier, puis le programme trouve et affiche 
inverse de ce nombre
'''


N=int(input("Veuillez saisir la valeur de N :"))
Inverse=0
while N !=0:
    Inverse = (Inverse*10)+(N%10)
    N=N//10
print("L'inverse de N est : ",Inverse)