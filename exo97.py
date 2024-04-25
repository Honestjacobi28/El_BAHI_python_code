
''' 
Creer un programme qui vous permet de saisir
les formules chimiques des molécules,d'organiser
une réaction chimique entre ces modécules et 
de vérifier si équation chimique de la réaction
est  équilibrée. Si l'équation n'est pas équilibrée,
le programme doit l'équilibrer

utiliser la librairie chemlib
'''

from chemlib import Compound,Reaction

methane=Compound("CH4")
oxygene=Compound("O2")
dioxyde_carbone=Compound("CO2")
eau=Compound("H2O")
print(methane.formula)
print(oxygene.formula)
print(dioxyde_carbone.formula)
print(eau.formula)
r=Reaction([methane,oxygene],[dioxyde_carbone,eau])
print(r.formula)
if r.is_balanced==False:
    r.balance()
print(r.formula)