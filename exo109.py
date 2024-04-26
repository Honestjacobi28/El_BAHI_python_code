''' 
Pour sa naissance , la grande-mère de Sara
place une somme de 1000€ sur son compte épargne
rémunéré au taux de 2%(chaque année le compte est augmenté de
2%). Ecrire un programme permettant afficher une liste 
sur 20 ans associants à chaque anniversaire de Sara
la somme acquise sur son compte.
'''

S=1000
C=[]

for i in range(80):
    S=S+S*0.02
    C.append(S)
    
for i,v in enumerate(C,start=1) : 
   print('à anniversaire',i,  'la somme est : ',format(v,'.2f'))

