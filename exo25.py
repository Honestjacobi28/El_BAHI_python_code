# STRUCTURES REPETITIVES

# Exercice 25

'''
Ecrire un programme qui demande un nombre de départ,et qui
ensuite affiche les dix nombres suivants en utilisant la
boucle for.Par exemple,si l'utilisateur entre le nombre 33
le programme affichera les nombres de 34 à 43
'''

N=int(input("Veuillez entrer un nombre : "))
print(f"les dix nombres apres {N} sont :")
''' 
range(a,b,c)
a=premier nombre
b=dernier nombre qui ne sera pas affiché
c=pas(par défaut= 1)
'''
for i in range(N+1,N+10+1):
    # end pour mettre sur la meme ligne
    print(i,end=" ")
    
