# -*- coding: utf-8 -*-
from random import randrange

#Fonction qui permet de simuler la génération de bits.
# donnée
# un entier n>0

# résultat
# une liste ca de n entiers de valeur  0 ou 1

def generation_Clef(n):
       ca=[]
       for i in range(0,n):
                 ca.append(randrange(0,2))          
       return ca
       
#Fonction qui permet de simuler la génération de la série de photons émis.
#Retourne une liste de symboles indiquant la polarisation :

# donnée
# un entier n>0
#une liste fa de n entiers de valeur  0 ou 1

# résultat
# une liste de n entiers constituée d'entiers compris entre 1 et 4

def generation_Photon(n,fa):
       photon=[]
       
       for i in range(0,n):
                 photon.append(randrange(1,5))          
       return photon
       	
#Retourne une liste de symboles indiquant la polarisation :
# donnée
# une liste fa d'entiers de valeur de 0 à 1
# une liste ca d'entiers de valeur de 0 à 1

# résultat
# une liste photon constituée d'entiers compris entre 1 et 4 respectant la polarisation des filtres
def generation_Photon_Alice(fa,ca):
	photon=[]
	for i in range(0,len(ca)):
		if fa[i]==1:
			if ca[i]==0:photon.append(1) 
			if ca[i]==1:photon.append(2) 
		if fa[i]==0:
			if ca[i]==0:photon.append(3) 
			if ca[i]==1:photon.append(4)         
	return photon

# donnée	
# un nombre entier f>0

# résultat
# une liste filtre contenant f valeurs binaires aléatoires

def generation_Filtre(f):
	filtre=[]
	for i in range(0,f):
          filtre.append(randrange(0,2))   
	return filtre


