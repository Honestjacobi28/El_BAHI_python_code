'''
Exo11

Ecrire un programme qui affiche la resistance équivalente à trois résistance R1,R2,R3:
  -Si les resistances sont branchées en série.
  -Si les resistances sont branchées en parallèle

'''

R1=float(input("entrez R1:"))
R2=float(input("entrez R2:"))
R3=float(input("entrez R3:"))
Rser=R1+R2+R310
Rpar=R1*R2*R3/(R1*R2+R1*R3+R2*R3)

print("la valeur en série est de:",format(Rser,".2f"))
print(f'la valeur en série est de:{format(Rpar,".2f")}')