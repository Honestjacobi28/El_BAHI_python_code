from voyage88 import voyage_frais as vf

nuits=int(input("Veuillez saisir le nombre de nuits: "))
ville=input("Veuillez saisir votre destination: ")
jours=int(input("Veuillez saisir le nombre de jours de location de voiture: "))
autres_frais=float(input("Veuillez saisir le total des autres frais: "))

cout = vf(nuits,jours,ville,autres_frais)
print("Le coup de total de votre voyage est : ",cout,"Euro")