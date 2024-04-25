'''
creer un programme qui permet de traduire un texte
d'une langue à une autre.

'''
# bibliothèque deep_translator
from deep_translator import GoogleTranslator

translated=GoogleTranslator(
                  source='auto',target='french'
                  ).translate("Let's keep in touch")
print(translated)