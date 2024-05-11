'''
Ecrire un programme utilisant une fonction qui détermine
si un nombre est premier ou non 
(rappel: un nombre premier n'est divisible que par 1 et
par lui-meme).
'''

def premier(N):
    estPremier=1
    for i in range(2,int(N/2)+1):
        if(N%i==0):
            estPremier=0
            break
        if estPremier==1:
            print(N,"est un nombre premier")
        else:
            print(N,"n'est un nombre premier")
            
N=int(input("Sasir un nombre: "))
premier(N)

for i in range(1,21):
    premier(i)