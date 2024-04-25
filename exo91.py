
"""
creer un programme qui permet de générer aléatoirement 
des: noms,dates de naissance,adresses,pays,empois,mail
et couleurs.
"""
# on va utiliser la biblothèque Faker

from faker import Faker

fake=Faker("fr_FR")
print(fake.name())
print(fake.date_of_birth())
print(fake.address())
print(fake.country())
print(fake.city())
print(fake.job())
print(fake.email())
print(fake.color_name())