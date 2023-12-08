# EXERCICE 14


'''
un magasin facture 0,30dh les dix premieres photocophies,0,25dh les vingt suivantes et 0,20 dh au-delà.
Ecrire un programme qui demande à l'utilisateur le nombre de photocophies effectuées et qui affiche 
la facture correspondante 
 
'''

nbre_photocopies=int(input('entrez le nombre de photocopies:'))

if nbre_photocopies<10:
    facture=nbre_photocopies * 0.30    
elif nbre_photocopies<30:
    facture= 10 * 0.30 + (nbre_photocopies-10) * 0.25 
elif nbre_photocopies<0:
    print("entrez un nombre valide")   
else:
    facture= 10 * 0.30 +20 * 0.25 + (nbre_photocopies-30) * 0.20    
print("votre facture est de :" , facture , "DH")
    