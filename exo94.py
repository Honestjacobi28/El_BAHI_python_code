'''
Créer un progamme qui permet d'afficher les informations
suivantes sur le virus corona:

* le nombre total des cas actifs
* le nombre total des confirmés  
* le nombre total récupérés
* le nombre total de décès
  
'''
 
# problème rencontré dans exécution de ce code
#sur la doc : https://pypi.org/project/covid/ 

from covid import Covid


covid=Covid()
# print(covid.get_data())
print(covid.list_countries())
print(covid.get_total_confirmed_cases())
print( covid.get_total_deaths())
print(covid.get_status_by_country_name("italy"))
