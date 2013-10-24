# -*- coding: utf-8 -*-

# donnée	
# une liste p de n entiers constituée d'entiers compris entre 1 et 4

# résultat
# une liste qb de n entiers égaux à 0 si p égal à 2 ou 4 et égaux à 1 si p égal 1 ou 4.

def qu_Bit(p):
	qb=[]
	for i in range(0,len(p)):
		if p[i]==1:qb.append(1)
		if p[i]==2:qb.append(0)
		if p[i]==3:qb.append(0)
		if p[i]==4:qb.append(1)
	return qb



