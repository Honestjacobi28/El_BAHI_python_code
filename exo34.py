'''
Ecrire un programme qui demande à utilasateur de taper
un entier n (rang)  et qui calcule le terme Un de la suite U
défini par: U0=6 Un+1= 4Un + 10
'''

n=int(input("Veuillez saisir indice n de la suite : "))

U=6

for i in range(1,n+1):
    U=4*U+10
print(f"U{n}=",U)

