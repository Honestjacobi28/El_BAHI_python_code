'''
Ecrire un programme qui calcule le pgcd de deux nombres 
entiers positifs
'''

a=int(input("Veuillez saisir la valeur de a :"))
b=int(input("Veuillez saisir la valeur de b :"))

if a>b:
    min=b
else:
    min=a
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        PGCD=i
print("Le PGCD de ",a," et ", b,"est: ",PGCD)
        