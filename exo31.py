'''
Ecrire un programme qui affiche les diviseurs
d'un entier positif n non nul

'''

# moi
'''
while True:
   n=int(input("Veuillez saisir un nombre : "))
   if n>0:
       break
for i in range(1,n+1):
    if (n%i)==0:
      print(f"les diviseurs de {n} sont:{i}",end=" ")
      
'''

# solution

N=int(input("Veuillez saisir la valeur de N: "))

while N<=0:
    N=int(input("Veuillez saisir la valeur de N: "))
print("Les diviseurs de 'N' sont: ")

for i in range(1,N+1):
    if (N%i==0):
      print(i,end=" ")
      