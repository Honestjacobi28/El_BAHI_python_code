'''
 Ecrire un programme qui demande à utlisateur
 de taper un entier n,puis qui calcule la somme
 des carrées des n premiers entiers impairs.
 
 Par ex , si n=5 le résultat est: 1ex2+3ex2+5ex2+7ex2+9ex2=165


'''

n=int(input("Veuillez entrer un entier: "))
S=0
j=1

#i ne sert qu'ici à faire des itérations 
for i in range(n):
    S=S+(j**2)
    j=j+2
print(f"La somme des carrées des {n}  premiers nombres impairs est :  {S}")
    
    
    