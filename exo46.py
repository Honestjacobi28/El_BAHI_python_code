'''
Ecrire un programme qui permet de convertir un nombre
décimal en binaire
'''

n=int(input("Veuillez saisir un nombre : "))
b=0
ord=0
while n!=0:
    reste=n%2
    p=10**ord
    b=b+reste*p
    #b+=reste*p
    ord+=1
    n=n//2
print(b)