''' 
 Ecrire un programme qui demande à utilisateur
 d'entrer 10 éléments stockés dans une liste L,
 puis le programme  détermine et affiche 
 le minimum et le maximum des éléments de la liste.
'''

L=[]

for i in range(1,11):
    print('L[',i,']=',end=' ')
    L.append(float(input()))
    
print(L)
print("Le maximum de la liste est: ",max(L))
print("Le minimum de la liste est: ",min(L))