import math
import statistics
import os #operating system
import random
import glob


with open('nombre.txt','w') as f:
    for i in range(20):
        f.write("{}^2 = {} \n".format(i, i**2))

#remplir une liste avec les éléments du fichier nombre 

#==============================================================================
#méthode 1


nombree=open('nombre.txt','r')
#print(nombree.read())    

with open('nombre.txt','r') as f:
    listenombre=f.read().splitlines()
    
    
#print(listenombre)
        
        


        
#==============================================================================
#méthode 2

methliste=[e.strip() for e in open('nombre.txt', 'r')]
#print(methliste, 'haha')




#==============================================================================
#exercice : dans le dossier, extraire tous les fichier.txt et stockeer dans chaque
#variable tout le contnu de chaque fichier
#==============================================================================

filee=glob.glob("*.txt")#pour enregistrer dans filenames
d={} # nous avons créer un dictionnaire car on ne peut pas créer une variable dans 
#une boucle for mais on peut créer une clé la-dedans

for file in filee:
    with open(file,'r') as f:
        d[file]=f.read().splitlines()
        
        
print(d)