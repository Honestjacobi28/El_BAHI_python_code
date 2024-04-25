'''
En important le module standard calendar, écrivez un 
programme qui demande à utilisateur de 
saisir l'année et le mois , puis le programme
affiche le calendrier de ce mois
'''

from calendar import month

yy=int(input("veuillez saisir une année: "))
mm=int(input("veuillez saisir un mois: "))

#display the calendar
print(month(yy,mm))