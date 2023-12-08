# EXERCICE


"""
Les produits vendus dans un magasin sont classés en trois catégorie de point de vue de TVA :
A=7% ,B=20%  et C=25%.Ecrivez un programme qui calcule le prix TTC d'un produit connaissant
son prix hors taxe et sa catégorie.                       
"""

HT = float(input("le prix hors taxe :"))
categorie = (input("la catégorie du produit A/B/C :"))

if categorie == "A":

    print("les prix TTC est de: ", format(HT*(1+0.07), ".2f"))
elif categorie == "B":

    print("les prix TTC est de: ", format(HT*(1+0.20), ".2f"))
elif categorie == "C":

    print("les prix TTC est de: ", format(HT*(1+0.25), ".2f"))

else:

    print("cette catégorie n'existe pas")
