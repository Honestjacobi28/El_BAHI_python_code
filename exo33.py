# Mardi 26

'''
 La population de la ville de Marrakech est de
 1,OOO,OOO d'habitants et elle augment 50,000
 habitants par an.Celle de la ville Agadir est 
 de 500,000 habts et elle augmentent de 8% par an.
 Ecrire un programme permettant de déterminer dans 
 combien d'années la population de la ville Agadir
 dépassera celle de la ville de Marraketch. 

'''

# mer 27 (36 37)(0/2)
# solution

p_aga=500000
p_ketch=1000000
nbr_ans=0

while p_ketch>p_aga:
    p_aga=p_aga*1.08
    p_ketch=p_ketch + 50000
    # nbr_ans+=1
    nbr_ans=nbr_ans+1
print("Agadir dépassera Marraketch après ",nbr_ans,"ans")
# ajouter par moi
print(f"p_ketch={p_ketch} p_aga={p_aga}")
    
# je vérifie mathématiquement
# En effet à 18ieme année p_aga=1 998 000  
# et p_ketch=1 900 000