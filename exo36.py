'''
Ecrire un progamme qui détermine si un nombre 
est premier ou non 

rappel: un nombre premier n'est divisible que par 1 et lui-meme
'''

N=int(input("saisir un nombre : "))
estPremier=1
for i in range(2,int(N/2)):
    if(N%i==0):
        estPremier=0
        break
if estPremier==1:
    print(N,"est un nombre premier")
else:
        print(N,"n \'est pas un nombre premier")

# je comprends pourquoi le programme indique que 4 est premier