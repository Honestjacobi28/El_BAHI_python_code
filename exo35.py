'''
suite de fibonacci

Ecrire un programme qui demande à utilisateur de taper 
un entier n supérieur à 2 jusqu'à ce que la reponse convienne
puis calcule et affiche tous les termes de la suite de Fibonacci
inférieurs ou égaux à n. La suite est définie comme suite :
UO=1 U1=1 Un+2= Un+1 + Un
'''

# suite de fibronacci
#exo inspiration
def fibonacci(n) :
 	# retourne une liste contenant la suite de fibonacci jusqu’à n
 	a = 0
 	b = 1
 	fib = [a]
    # ajouter = pour afficher les nombres de la suite <= n
 	while b <= n :
 		a, b = b, a+b
 		fib.append(a)
 	return fib

# print(fibonacci(13))



# recherche (bug avec n<2) 
'''n= int(input("saisir n:  "))
n>2

U0=0
U1=1
list_fib=[U0]

while U1 <= n:
 		U0, U1 = U1, U0+U1
 		list_fib.append(U0)
print(list_fib)'''    


#solution
n=int(input("veuillez saisir le rang : "))

while n<2:
    n=int(input("veuillez saisir le rang : "))

# Upp=UO Up=U1

Upp=0
Up=1

print("Les termes de la suite de Fibonacci sont :")
print(Upp,end=" ")
print(Up,end=" ")
for i in range(n-1):
    U=Upp + Up
    print(U,end=" ")
    Upp=Up
    Up=U

    