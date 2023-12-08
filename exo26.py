
# Exercice 26

'''
Ecrire un programme qui demande un nombre de départ,et qui
ensuite affiche les dix nombres suivants en utilisant la
boucle while.Par exemple,si l'utilisateur entre le nombre 33
le programme affichera les nombres de 34 à 43
'''

N=int(input("Veuillez entrer un nombre : "))
print(f"les dix nombres apres {N} sont :")

i=N+1
while i<=N+10:
    print(i,end=" ")
    i+=1