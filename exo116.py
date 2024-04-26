''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 nombres stockés dans une liste L,
 ensuite , le programme à aide 
 d'une fonction déplace tous les nombres
 négatifs au début et positifs à la fin de L.
'''

def deplacer(L):
    j=0
    for i in range(10):
        if(L[i]<0):
            L[i],L[j]=L[j],L[i]
            j+=1
    print(L)
    
L=[]

for i in range(10):
    print('L[',i,']=',end=' ')
    L.append(int(input()))
print(L)
deplacer(L)