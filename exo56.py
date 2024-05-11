'''
Ecrire un programme permettant de  tracer 
la lettre A (nombre de lignes : 7)

              * * *   
            *       * 
            *       * 
            * * * * * 
            *       * 
            *       * 
            *       *

      
'''

L=int(input("Saisir le nombre de lignes: "))
for i in range(1,L+1):
    for j in range(1,6):
        if (j==1 or j==5) and (i!=1):
            print("* ",end="")
        elif(i==1 or i==(L+1)//2) and (j>1 and j<5):
            print("* ",end="") 
        else:   
            print("  ",end="")
    
    print()
    
