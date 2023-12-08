# EXERCICE  15
'''
Ecrire un programme qui demande l'age d'un enfant à l'utilisateur .
Ensuite, il informe de sa categorie:"Poussin" de 6 à 7 ans, "Pupille" 
de 8 à 9 ans , "Mimime" de 10 à 11 ans,"Cadet" après 12
'''


age_enfant= int(input("entrez l'age de l'enfant: "))

if age_enfant>=6 and age_enfant<=7:
   print( "l'enfant dans la categorie: Poussin")
   
elif age_enfant>=8 and age_enfant<=9:
    print("l'enfant est dans la categorie: Pupille")
elif age_enfant>=10 and age_enfant<=11:
    print("l'enfant est dans la categorie: Mimime")
elif age_enfant>=12 and age_enfant<=16:
    print("l'enfant est dans la categorie: Cadet")
    
else:
   print("la categorie n'existe pas")