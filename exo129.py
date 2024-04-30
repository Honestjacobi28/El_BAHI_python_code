'''
Ecrire un programme qui détermine
la ligne dans une matrice dont
la somme de ses éléments est 
la plus grande
'''

M=[
    [6,8,1,6],
    [3,5,6,20],
    [2,2,8,85],
    [5,2,19,20]
]

print(max(M))

L=max(M,key=sum)
print('La liste avec la somme la plus grande est : ',L)