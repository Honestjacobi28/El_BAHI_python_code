# EXERCICE

'''
Ecrire un programme permettant de saisir trois notes (sur 20) d'un etudiant,calculant
sa moyenne et affichant cette moyenne avec la mention("très bien" à partir de 16 , "bien"
entre 14 et 16, "assez bien" entre 12 et 14 , "passable"  entre 10 et 12, "insuffisant"
en dessous de 10)

PS:En suppose que l'étudiant va saisir des notes comprises entre 0 et 20. 
'''

print("veuillez saisir vos notes")

N1=float(input('note 1 :'))
N2=float(input('note 2 :'))
N3=float(input('note 3 :'))
MOY=(N1+N2+N3)/3

print("la moyenne est l'étudiant de :",format(MOY,".2f"))
if MOY<10:
    print(" mention:Insuffisant ")
    
elif MOY>=10 and MOY<12:
    print(" mention:Passable ")
            
elif MOY>=12 and MOY<14:
    print("mention: Assez Bien")
    
elif MOY>=14 and MOY<16:
    print(" mention:Bien")
    
else:
    print("mention:Très bien")


# code optimiser pck MOY est affiché une fois
    

    

    
    
