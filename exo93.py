'''
creer un programme qui permet de tester la vitesse
de votre internet: téléchargement(download)
et transfert(upload).
'''

import speedtest

st= speedtest.Speedtest()

print("Wifi Download Speed is ",(st.download())/1024,"mo")
print("Wifi Upload Speed is ",st.upload()/1024,"mo")