'''
Ecrire un programme qui permet d'afficher
une liste des n premiers nombres premiers
n est un nombre entier saisi par 
utilisateur.
'''

n=int(input("Veuillez entrer la valeur de n : "))
P=[]
x=2

while True:
    #a
    estPremier=0
    
    #b
    for i in range(2,x):
        if x%i==0:
            estPremier=1
            break
        
    #c
    if estPremier==0:
        P.append(x)
    #d
    x+=1

    #e
    if len(P)==n:
        break
print("les",n,"premiers nombres premiers sont : \n ",P)