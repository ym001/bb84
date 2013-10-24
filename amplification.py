# -*- coding: utf-8 -*-
from random import randrange
import math

# donnée	
# une liste l de n entiers constituée d'entiers compris entre 0 et 1.

# résultat
# une liste p de n entiers constituée d'entiers compris entre 0 et 1.
# dont le mélange est reproductible

def amplification_Clef(l):
	p=[]
	while l:
		x=len(l)
		f=randrange(0,2)
		if f==0:i=f1(x)
		if f==1:i=f2(x)
		p.append(l[i])
		l.pop(i)
	for i in range(0,int(len(p)/2)):
		p.pop()

	return p

# donnée	
# x un nombre entier

# résultat
# i un nombre entier image de f1

def f1(x):
	i=int(x*x*math.pi)%x
	return i
	
# donnée	
# x un nombre entier

# résultat
# i un nombre entier image de f1
	
def f2(x):
	i=int(x*x*x*math.pi)%x
	return i

