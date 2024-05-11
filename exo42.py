'''
Ecrire un programme qui vérifie si nombre est palindrome
ou non. (rappel:Un nombre palindrome est un nombre qui peut
se lire indifférent de gauche et à droite ou de 
droite à gauche,eg:161)
'''

N=int(input("Veuillez saisir la valeur de N: "))
M=N
Inverse=0
while N !=0:
    Inverse=(Inverse*10)+(N%10)
    N=N//10
if M==Inverse:
    print(M,"est un nombre palindrome")
else:
    print(M,"est un nombre non palindrome")
    
    