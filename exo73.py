'''
Ecrire un programme qui demande à utilisateur de saisir
une année et qui utilise une fonction pour vérifier
si année est bissextile(366 jours) ou non
'''

def type_annee(A):
    if (A % 4==0 and A % 100 !=0)or (A%400==0):
        print(A,"est une année bissextile")
    else:
        print(A,"n'est pas une année bissextile")
        
A=int(input("Veuillez saisir une année :"))
type_annee(A)


for i in range(2000,2024):
    type_annee(i)