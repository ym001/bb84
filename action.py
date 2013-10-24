# -*- coding: utf-8 -*-
from random import randrange
import math

# donnée	
# une liste l de n entierss constituée d'entiers compris entre 1 et 4
# x un entier compris entre 0 et n

# résultat
# une liste l de n entiers constituée d'entiers compris entre 1 et 4 et de x entiers de valeurs modifiée entre 1 et 4.

def bruit_Photon(l,x):
	for i in range(0,x):
		l[randrange(0,len(l))]=randrange(1,5)
	return l

# donnée	
# une liste l de n entiers constituée d'entiers compris entre 1 et 4
# x un entier compris entre 0 et 100

# résultat
# une liste l de n entiers constituée d'entiers compris entre 1 et 4 et de x entiers égal à -1.

def perte_Photon(l,x):
	i=0
	while i<x:
		rang=randrange(0,len(l))
		while l[rang]==-1:
			rang=randrange(0,len(l))
		l[rang]=-1
		i=i+1
	return l

# donnée	
# une liste pb de n entiers constituée d'entiers compris entre 1 et 4
# une liste fa de n entiers constituée d'entiers compris entre 1 et 0
# une liste fb de n entiers constituée d'entiers compris entre 1 et 0

# résultat
# une liste pb de n entiers compris entre 1 et 4 et de x entiers égal à -1 lorsque pa different pb.

def perte_Photon_Lecture(pb,fa,fb):
	for i in range(0,len(pb)):
		if fa[i]!=fb[i]:pb[i]=-1
	return pb

	
# donnée	
# une liste pa de n entiers constituée d'entiers compris entre -1 et 4
# une liste pb de n entiers constituée d'entiers compris entre -1 et 4
# une liste fa de n entiers constituée d'entiers compris entre -1 et 0
# une liste fb de n entiers constituée d'entiers compris entre -1 et 0

# résultat
# une liste pa de n entiers constituée d'entiers compris entre 1 et 4
# une liste pb de n entiers constituée d'entiers compris entre 1 et 4
# une liste fa de n entiers constituée d'entiers compris entre 1 et 0
# une liste fb de n entiers constituée d'entiers compris entre 1 et 0
#les cellules de rang identique ou pb égal à -1 sont supprimées
	


def photon_Manquant(pa,pb,fa,fb):
	a=[]
	b=[]
	c=[]
	d=[]
	while pa:
		x = pa.pop()
		y = pb.pop()
		z = fa.pop()
		w = fb.pop()
		if y!=-1:
			a.append(x)
			b.append(y)
			c.append(z)
			d.append(w)
	a.reverse() #necessaire si on veut conserver l'ordre initial des éléments
	b.reverse() 
	c.reverse()
	d.reverse() 
	pa = a
	pb = b
	fa = c
	fb = d
	return  pa,pb,fa,fb
	
# donnée	
# une liste pa de n entiers constituée d'entiers compris entre 1 et 4
# nb un entier compris entre 0 et 100
# np un entier compris entre 0 et 100
# une liste fa de n entiers constituée d'entiers compris entre 1 et 0
# une liste fb de n entiers constituée d'entiers compris entre 1 et 0

# résultat
# une liste de pb d'entiers constituée d'entiers compris entre 1 et 4 ayant subi les fonctions bruit_Photon, perte_Photon et perte_Photon_Lecture.	
	
def photon_Transmission(pa,nb,np,fa,fb):
	pb=[]
	for i in range(0,len(pa)):
		pb.append(pa[i])
	pb=bruit_Photon(pb,nb)
	pb=perte_Photon(pb,np)
	pb=perte_Photon_Lecture(pb,fa,fb)

	return pb

# donnée	
# une liste pa de n entiers constituée d'entiers compris entre 1 et 4
# une liste pb de n entiers constituée d'entiers compris entre 1 et 4
# une liste fa de n entiers constituée d'entiers compris entre 1 et 0
# une liste fb de n entiers constituée d'entiers compris entre 1 et 0

# résultat
# une liste pa de n entiers constituée d'entiers compris entre 1 et 4
# une liste pb de n entiers constituée d'entiers compris entre 1 et 4
# une liste fa de n entiers constituée d'entiers compris entre 1 et 0
# une liste fb de n entiers constituée d'entiers compris entre 1 et 0
#les cellules de rang identique ou fa est égal à fb sont conservées les autres sont supprimées
	
def filtre_Comparaison(pa,pb,fa,fb):
	a=[]
	b=[]
	c=[]
	d=[]
	while pa:
		x = pa.pop()
		y = pb.pop()
		z = fa.pop()
		w = fb.pop()
		if w==z:
			a.append(x)
			b.append(y)
			c.append(z)
			d.append(w)
	a.reverse() #necessaire si on veut conserver l'ordre initial des éléments
	b.reverse() 
	c.reverse()
	d.reverse() 
	pa = a
	pb = b
	fa = c
	fb = d
	return pa,pb,fa,fb
	



	
# donnée	
# une liste pa de n entiers constituée d'entiers compris entre 1 et 4
# une liste pb de n entiers constituée d'entiers compris entre 1 et 4

# résultat
# une liste  d'entiers constituée des valeurs communes de pb et pa.

def comparaison_Photon(pb,pa):
	p=[]
	for i in range(0,len(pb)):
		if pb[i]==pa[i] and pb[i]!=0:p.append(pb[i])
	return p
	
# donnée	
#une liste la d'entiers contenant des valeurs (1,2,3,4)
#une liste lb d'entiers contenant des valeurs (1,2,3,4)
#na nombre entier de photons differents acceptable

# résultat
# retourne vrai si le nombre de différences entre la et lb est supérieur à na

def detection_Pirate(la,lb,na):
	e=0
	for i in range(0,len(la)):
		if la[i]!=lb[i]:
			e=e+1		
	if e>na:
		d=True	
	else: 
		d=False

	return d
	
# donnée	
#une liste l d'entiers contenant des valeurs (1,2,3,4)

# résultat	
#une liste l d'entiers contenant des valeurs (1,2,3,4) ayant subit la fonction bruit_Photon
def piratage(l,x):
	l=bruit_Photon(l,x)
	return l


# donnée	
#une liste ca d'entiers contenant des valeurs 0 ou 1
#une liste cb d'entiers contenant des valeurs 0 ou 1
#un entier b

# résultat	
#un booléen vrai s'il existe au moins une difference entre ca et cb et faux sinon

def comparaison_Clef_Finale(ca,cb):
	erreur=False
	i=0
	while i<len(cb) and erreur==False:
		if ca[i]!=cb[i]:erreur=True
		i=i+1
	return erreur
	

	
# donnée	
#un entier a
#un entier b
# résultat	
#un réel résultat de a/b

def taux_De_Transfert(a,b):
	r=a/b
	return r


