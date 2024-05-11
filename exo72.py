'''
FONCTIONS ET MODULES

Ecrire  un programme utilisant une fonction qui affiche
le cube d'un nombre réel saisi au clavier
'''

def cube(N):
    return N*N*N

N=int(input("Veuillez saisir un nombre:  ")) 
print("Le cube de",N,"est: ",cube(N))       


for i in range(1,11):
    print("Le cube de",i,"est: ",cube(i))    
    