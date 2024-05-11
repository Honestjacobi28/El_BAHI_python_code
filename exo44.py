'''
Ecrire un  programme qui verifie si un nombre est parfait
ou non. un nombre est dit parfait s'il est égal à la somme
de ses diviseurs propres (diviseurs de ce nombre 
autres que lui-meme )
'''

n=int(input("Veuillez saisir un nombre :"))
S=0
for i in range(1,n):
    if n%i==0:
        S=S+i
if n==S:
    print(n,"est un nombre parfait ")
else:
    print(n,"est un nombre non parfait ")
        