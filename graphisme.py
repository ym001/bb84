# -*- coding: utf-8 -*-


# donnée
# Une liste de photons d'entiers compris entre 1 et 4
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type photon. 

def affiche_Photon(photon,ligne,caractere):
	if photon==-1:
		x1=0
		y1=0
		x2=0
		y2=0
	if photon==1:
		x1,y1,x2,y2=coord_Photon_Vertical(ligne,caractere)
	if photon==2:
		x1,y1,x2,y2=coord_Photon_Horizontal(ligne,caractere)
	if photon==3:
		x1,y1,x2,y2=coord_Photon_Oblique(ligne,caractere)
	if photon==4:
		x1,y1,x2,y2=coord_Photon_Oblique_Inverse(ligne,caractere)
	return x1,y1,x2,y2
	
# donnée
# Une liste filtre d'entiers compris entre 0 et 1
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type filtre. 	

def affiche_Filtre(filtre,ligne,caractere):
	if filtre==-1:
		xa1=0
		ya1=0
		xa2=0
		ya2=0
		xb1=0
		yb1=0
		xb2=0
		yb2=0

	if filtre==1:
		xa1,ya1,xa2,ya2=coord_Photon_Vertical(ligne,caractere)
		xb1,yb1,xb2,yb2=coord_Photon_Horizontal(ligne,caractere)

	if filtre==0:
		xa1,ya1,xa2,ya2=coord_Photon_Oblique(ligne,caractere)
		xb1,yb1,xb2,yb2=coord_Photon_Oblique_Inverse(ligne,caractere)
	return xa1,ya1,xa2,ya2,xb1,yb1,xb2,yb2
	
# donnée
# Une liste clef d'entiers compris entre 0 et 1
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type clef. 		
	
def affiche_Clef(clef,ligne,caractere):
	x1,y1=coord_Caractere(ligne,caractere)
	return x1,y1

# donnée
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type photon horizontal. 	

def coord_Photon_Horizontal(ligne,caractere):
	hauteurl=10
	longueurc=10
	hauteurc=10
	espacex=2
	espacey=5
	positionxc=(longueurc+espacex)*caractere
	positionyc=(hauteurl+espacey)*ligne
	x1=positionxc
	y1=positionyc-int(hauteurl/2)
	x2=positionxc+longueurc
	y2=positionyc-int(hauteurl/2)
	return x1,y1,x2,y2
	
# donnée
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type photon vertical. 	
	
def coord_Photon_Vertical(ligne,caractere):
	hauteurl=10
	longueurc=10
	hauteurc=10
	espacex=2
	espacey=5
	positionxc=(longueurc+espacex)*caractere
	positionyc=(hauteurl+espacey)*ligne
	x1=positionxc+int(longueurc/2)
	y1=positionyc
	x2=positionxc+int(longueurc/2)
	y2=positionyc-hauteurc
	return x1,y1,x2,y2

# donnée
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type photon oblique. 	

def coord_Photon_Oblique(ligne,caractere):
	hauteurl=10
	longueurc=10
	hauteurc=10
	espacex=2
	espacey=5	
	positionxc=(longueurc+espacex)*caractere
	positionyc=(hauteurl+espacey)*ligne
	x1=positionxc
	y1=positionyc
	x2=positionxc+longueurc
	y2=positionyc-hauteurc
	return x1,y1,x2,y2

# donnée
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type photon oblique inverse. 	

def coord_Photon_Oblique_Inverse(ligne,caractere):
	hauteurl=10
	longueurc=10
	hauteurc=10
	espacex=2
	espacey=5
	positionxc=(longueurc+espacex)*caractere
	positionyc=(hauteurl+espacey)*ligne
	x1=positionxc
	y1=positionyc-hauteurc
	x2=positionxc+longueurc
	y2=positionyc
	return x1,y1,x2,y2
	
# donnée
# ligne un entier positif
# caractère un entier positif

# résultat
# Retourne les coordonnées graphiques de la représentation graphique du type clef. 		
def coord_Caractere(ligne,caractere):
	
	hauteurl=10
	longueurc=10
	hauteurc=10
	espacex=2
	espacey=5
	positionxc=(longueurc+espacex)*caractere
	positionyc=(hauteurl+espacey)*ligne-hauteurc
	x1=positionxc
	y1=positionyc
	return x1,y1

	
	return x,y
