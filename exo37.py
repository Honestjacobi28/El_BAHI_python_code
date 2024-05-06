'''
Ecrire un programme qui demande à utilisateur de 
saisir le nombre d'équipes participant à un 
championnat , puis le programme affiche la 
liste des matchs à domicile et à extérieur
pour ce championnat
'''

n=int(input("Veuillez entrer le nombre d'équipes : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j:
            print("Equipe",i,"VS Equipe",j)