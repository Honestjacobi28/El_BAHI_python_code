'''
EXO27
Ecrire un programme qui affiche la somme:
S=1+1/10+1/1000+...+1/10exposantn 

'''

n=int(input("Entrer la valeur de n :"))
S=0

for i in range(1,n+1):
    S+=(1/i)
print(f"la somme de la serie est de :{S}")