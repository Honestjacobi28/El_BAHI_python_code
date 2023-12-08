'''Ecrire un programme qui demande un temps T(entier) 
exprimé en secondes, et qui le convertit en heures,minutes,secondes.
Ex: T=56263S = 15H 37M  43S
'''


T= int(input("quel est la durée seconde : "))
H = T // 3600
R = T % 3600
M = R//60
S=R%60

print(T,"s =",H,"H",M,"min",S,"s")
