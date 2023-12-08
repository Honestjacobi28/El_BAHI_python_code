# lundi 25 sept 2023(entre 11h et 12h)

# Je dois suivre les tutos 32 et 33 (1/2)

'''
 A la naissance de Amal,son grand-père Ali,lui ouvre
 un compte bancaire.Ensuite,à chaque anniversaire,
 le grand-père  de Amal verse sur son compte 500dh,auquels
 il ajoute le triple de age de Amal.Par exemple,
 lorsqu'elle a 4 ans, il lui verse 512 dh . Ecrire un
 programme qui permette de déterminer quelle somme
 aura Amal lors n-iéme anniversaire.
'''

# moi
N=int(input("Veuillez saisir le nombre nombre Année: "))
S=0

for i in range(1,N+1):
    # S=S+(500 + (3*N))
    # Solution
    # *i au lieu de *N
    S=S+(500 + (3*i))
print(f"la somme à {N}-ième année est de :{S} DH")

# Mardi 26
#  Je dois suivre les tutos 34 et 35 (0/2)