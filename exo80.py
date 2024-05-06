'''
Ecrire une fonction affiche_employe() de telle sorte qu'elle
accepte le nom de l'employé et son salaire et affiche les 
deux. Si salaire manque dans l'appel de la fonction,attribuez la
valeur par défaut 3000 au salaire
'''

def affiche_employe(nom,salaire=3000):
    print("le salaire de employé",nom,"est",salaire,"€")
    
affiche_employe("Koffi",4600)
affiche_employe("Konan")