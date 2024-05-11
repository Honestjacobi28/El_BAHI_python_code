'''
Ecrire un programme qui vérifie si un nombre est parfait ou non.
Un nombre est dit parfait s'il est égal à la somme de des 
diviseurs propres(diviseurs de ce nombre autres que lui-meme)

'''

def parfait(n):
    S=0
    for i in range(1,n):
        if n%i==0:
            S+=i
    if n==S:
        print(n)
        
print("les nombres parfaits entre 1 et 1000 sont: ")            
for i in range(1,1000):
    parfait(i)