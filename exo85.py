'''
Creer un programme qui permet de tester la conjecture 
de la suite de Syracuse.

Un+1{
    Un/2 si Un est pair
    3Un +1 si Un est impair
}


'''

def syracuse(U):
    while U!=1:
        if U%2==0:
            U//=2
        else:
            U=3*U+1
        print(U)

U=int(input("Veuillez entrer le premier terme :"))
if U>0:
    print(U)
    syracuse(U)
else:
    print("suite pas défini")
    
# on termine tjr par 1 pour U>0