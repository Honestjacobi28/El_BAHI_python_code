'''
EXO28
Ecrire un programme qui affiche la somme:
S=1+10+1000+...+10exposantn 
'''
# moi
'''
n=int(input("Entrer la valeur de n :"))

sn=(1-(10**n*10))/(1-10)

print(f"la valeur de la somme est de:{sn}")

'''
# solution

n=int(input("Entrer la valeur de n :"))
S=0

for i in range(0,n+1):
    S+=(10**i)
print(f"la somme de la serie est de :{S}")