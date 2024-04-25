'''
 Ecrire un programme qui permet de convertir le 
 texte en parole
'''

import pyttsx3

engine=pyttsx3.init()
voice=engine.getProperty('voices')[0] # french voice
engine.setProperty('voice',voice.id)

engine.say("je m'appelle Jean-Fabrice OUFFOUE.")

engine.runAndWait()