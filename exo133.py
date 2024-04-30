'''
Ecrire un programme qui permet de trouver 
le nombre mystère qui remplit les conditions
suivantes:
- il est composé de 3 chiffres;
- il est strictement supérieur à 500;
- Il est impair;
- Deux de ses chiffres sont identiques.
- La somme de ses chiffres est 9.  
'''

def cond4(e):
    if e[0]==e[1] or e[0]==e[2] or e[1]==e[2]:
        return True 
    else:
        return False
    
def cond5(e):
    if int(e[0])+int(e[1])+int(e[2])==9:
        return True
    else:
        return False
    
L=list(range(501,1000,2))
for e in L:
    e=str(e)
    if cond4(e) and cond5(e):
        print(e)