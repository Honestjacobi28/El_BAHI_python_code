#  STRUCTURES CONDITIONNELLES


'''
 Exo12
  Ecrire un programme qui retourne si deux nombres entiers donnés sont de meme signe ou non 

'''


A=int(input("Entrez A:"))
B=int(input("Entrez B:"))
AB=A*B
if AB>0:
    print("AB=",AB,":A et B sont de memes signes")
else:
    print("AB=",AB,":A et B sont de signes contraires")

    