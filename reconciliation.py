# -*- coding: utf-8 -*-
from random import randrange

# donnée	
# une liste la de n entiers constituée d'entiers compris entre 0 et 1
# une liste lb de n entiers constituée d'entiers compris entre 0 et 1

# résultat
#retourne tb un nombre entier indiquant la moyenne(entière) d'erreurs dans les 10% premiers éléments.

def taille_Bloc(la,lb):	
	erreur=0
	for i in range(0,len(lb)):
		if la[i]!=lb[i]:
			erreur=erreur+1
	if erreur!=0:
		tb=int(len(lb)/erreur)
	else: 
		tb=len(lb)	
	return tb

# donnée	
# une liste la de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# retourne les listes lb en ayant supprimé les 10% premiers éléments des listes.

def sup_Bloc_Connu(la):
	echantillon=int(10/100*len(la))
	for i in range(0,echantillon):
		del la[i]
	return la
	
# donnée	
# une liste la de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# retourne une listes l et pa en ayant conservé les 10% premiers éléments de la liste.

def bloc_Connu(la):
	l=[]
	echantillon=int(10/100*len(la))
	for i in range(0,echantillon):
		l.append(la[i])
	return l
	
# donnée	
# une liste la de n entiers constituée d'entiers compris entre 0 et 1
#un entier tb

# résultat
# une liste de listes m constituée de liste de taille tb d'entiers compris entre 0 et 1

def decoupage_En_Bloc(la,tb):
	m=[]
	fin =len(la)//tb
	for i in range(0,fin):
		m.append([])
		for j in range(0,tb):
			m[i].append(la[i*tb+j])
	return m

# donnée	
# une liste de listes m1 constituée d'entiers compris entre 0 et 1
# une liste de listes m2 constituée d'entiers compris entre 0 et 1

# résultat
# une liste de listes m résultat de m1*m2 mod2

def multiplication_Matrice(m1, m2): 
	m = [] 
	for i in range(len(m1)): 
		element =0
		for j in range(len(m1[0])): 
			element = (element +m1[i][j]*m2[j])%2
		m.append(element) 
	return m 
	
# donnée	
# une liste constituée d'entiers compris entre 0 et 1
# une liste constituée d'entiers compris entre 0 et 1

# résultat
# une liste constituée des indices des différences entre la et lb

def comparaison_Clef(la, lb): 
	lerreur=[]
	for i in range(len(lb)): 
		if la[i]!=lb[i]:lerreur.append(i)
	return lerreur 


# donnée	
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1
#ou m*h=0
def construction_Bit_De_Parite_Hamming(ma,mb):
	lparite=[]
	matrice_generatrice=[[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	for i in range(0,len(ma)):
		lparite=multiplication_Matrice(matrice_generatrice, ma[i])	
		d0=mb[i][0]#bit transmis p_1 p_2 d_1 p_3 d_2 d_3 d_4
		d1=mb[i][1]
		d2=mb[i][2]
		d3=mb[i][3]
		lp=[lparite[0],lparite[1],d0,lparite[3],d1,d2,d3]#alice transmet les bits de parité à bob sans erreur
		mb[i]=lp

	return mb
	
# donnée	
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# mb corrigé par le syndrome

def correction_erreur_Hamming(mb):
	ma=[]
	mbx=[]
	mb=[]
	matrice_generatrice=[[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]]
	for i in range(0,len(mb)):
		mbx=multiplication_Matrice(matrice_generatrice, mb[i])	
		x=mbx[0]+2*mbx[1]+4*mbx[2]#la valeur décimale du mot binaire indique une erreur si elle n'est pas égale à zéro.
		if x!=0:
			for j in range(0,7):
				if j==x:me.append(1)
				else:me.append(0)
			for j in range(0,7):
				mb[j]=me[j]+mb[j]
			mb[i]=mb				#correction de l'erreur
		
	return mb
	
# donnée	
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1
# tb un nombre entier

# résultat
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1
# ou on rajoute à la fin des listes la parité de la liste.

def ajout_Bit_De_Parite(ma,tb):
	for i in range(0,len(ma)):
		c=0
		for j in range(0,tb):
			if ma[i][j]=="1":
				c=c+1
		parite=c%2
		ma[i].append(parite)
	return ma

# donnée	
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1
#les listes différentes entre ma et mb sont supprimées
def comparaison_Des_Bits_De_Parite(ma,mb,tb):
	a=[]
	b=[]
	while ma:
		x = ma.pop()
		y = mb.pop()
		if x[tb]==y[tb]:
			a.append(x)
			b.append(y)
	a.reverse() #necessaire si on veut conserver l'ordre initial des éléments
	b.reverse()
	ma = a
	mb = b
	return ma,mb
	
	
# donnée	
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1.

# résultat
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1.
#la dernière cellule des listes est supprimée

def destruction_Bit_Parite(mb):
	for i in range(0,len(mb)):
		      mb[i].pop()
	return mb
	
# donnée	
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# une liste de listes mb de n entiers constituée d'entiers compris entre 0 et 1
#constituée des rangs 2,4,5,6

def destruction_Bit_Parite_Hamming(mb):
	m=[]
	for i in range(0,len(mb)):
		     m[i].append (mb[2])
		     m[i].append (mb[4])
		     m[i].append (mb[5])
		     m[i].append (mb[6])
	return m
	
	
# donnée	
# une liste de listes ma de n entiers constituée d'entiers compris entre 0 et 1

# résultat
# une liste la de n entiers constituée des listes de ma mis en ligne 

def reconstruction_Clef(ma):
	la=[]
	for i in range(0,len(ma)):
		for j in range(0,len(ma[i])):
		      la.append(ma[i][j])
	return la

# donnée	
# une liste la de n entiers de valeur 0 ou 1
# une liste lb de n entiers de valeur 0 ou 1

# résultat
# une liste ca de n entiers de valeur 0 ou 1
# une liste cb de n entiers de valeur 0 ou 1
# ayant subi les fonctions étapes de la réconciliation

def reconciliation_Parite_Simple(la,lb):
	
	ma=[]
	mb=[]
	tb=taille_Bloc(la,lb)
	ma=decoupage_En_Bloc(la,tb)
	mb=decoupage_En_Bloc(lb,tb)
	ma=ajout_Bit_De_Parite(ma,tb)
	mb=ajout_Bit_De_Parite(mb,tb)
	ma,mb=comparaison_Des_Bits_De_Parite(ma,mb,tb)
	ma=destruction_Bit_Parite(ma)
	mb=destruction_Bit_Parite(mb)
	ca=reconstruction_Clef(ma)
	cb=reconstruction_Clef(mb)

	return cb


# donnée	
# une liste la de n entiers de valeur 0 ou 1
# une liste lb de n entiers de valeur 0 ou 1

# résultat
# une liste ca de n entiers de valeur 0 ou 1
# une liste cb de n entiers de valeur 0 ou 1
# ayant subi les fonctions étapes de la réconciliation

def reconciliation_Parite_Hamming(la,lb):
	ma=[]
	mb=[]
	la=sup_Bloc_Connu(la)
	lb=sup_Bloc_Connu(lb)
	ma=decoupage_En_Bloc(la,4)
	mb=decoupage_En_Bloc(lb,4)
	mb=construction_Bit_De_Parite_Hamming(ma,mb)
	mb=correction_erreur_Hamming(mb)
	mb=destruction_Bit_Parite_Hamming(mb)
	cb=reconstruction_Clef(mb)
	return cb
	
	
	



	

