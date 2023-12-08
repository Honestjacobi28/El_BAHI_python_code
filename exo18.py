# EXERCICE


"""
 Les habitants d'une ville paient l'impôt selon les règles suivantes :
 - Les de plus de 20 ans paient l'impôt 
 - Les femmes paient l'impôt si elles ont entre 18 et 35 ans
 - Les autres ne paient pas d'impôt
 Ecrire un programme qui demande l'age et le sexe d'un habitant et affiche 
 si celui-ci est imposable. 
"""

# METHODE 1
"""
age=int(input("votre age : "))
sexe=(input("votre sexe H ou F : "))

if age>20 and sexe=="H":
    print("vous etes imposable")
elif (age>=18 and age<=35) and sexe=="F":
    print("vous etes imposable")
else:
   print("vous etes non imposable") """
   
# ou mieux  methode 2  

"""
sexe= input("votre sexe H/F :")
age= int(input("votre age  :"))

if ( (sexe=="H" and age>=20) or (sexe=="F" and age>=18 and age<=35)):
    print("vous etes imposable")
else:
    print("vous etes non imposable")
"""

# METHODE 3


sexe= input("votre sexe H/F :")
age= int(input("votre age  :"))

R1= sexe=="H" and age>=20
R2= sexe=="F" and age>=18 and age<=35

if R1 or R2:
    print("vous etes imposable")
    
else:
    print("vous etes non imposable")

    
