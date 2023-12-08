'''
 Ecrire un programme qui échange les contenus de deux données numeriques si elles sont de meme signe,
 sinon il met la somme des deux dans la première donnée et leur produit dans la seconde  
'''

A=int(input("Entrer A:"))
B=int(input("Entrer B:"))
AB=A*B

if(AB>0):
    A,B=B,A   
else:
    S=A+B
    P=AB
    A=S
    B=P
print("la nouvelle valeur de A est:",A)
print("la nouvelle valeur de B est:",B)