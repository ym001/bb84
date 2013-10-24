import tkinter
#! /usr/bin/env python3.1
# -*- coding: utf-8 -*-
#auteur:Yves Mercadier Daniel Veissi
import sys
import tkinter


from action import *
from amplification import *
from codage import *
from generateur import *
from graphisme import *
from reconciliation import *

list_action=["Alice génère une clef","Alice génère une suite de filtre.","Alice envoie les photons.","Bob mesure.","Bob lit.","Bob annonce la base choisie.","Bob et alice comparent leur base.","Alice et Bob analysent les données.","Clef secrète réconciliée.","Clef secrète amplifiée."]
etape=0
compteur=1
reconciliation=0
pirate=False
erreur=False
nombre_photon=500
valeur_perte=5
valeur_bruit=5
ligne=0

# donnée
# une liste l d'entiers compris entre -1 et 4

# résultat
# affiche une étape du protocole BB85

def affiche_Etape(l):
	global erreur	
	global etape	
	global nombre_photon
	global ligne
	if etape==0:
		nombre_photon=nombre_photon_emis.get()
		largeur=int(nombre_photon*12)
		can2.config(width=largeur)
		can1.create_text(0,ligne*15, text="n°"+str(compteur),anchor=tkinter.NW)
		can2.create_text(0,ligne*15, text="n°"+str(compteur),anchor=tkinter.NW)
		ligne=ligne+1
		ligne=ligne+1

		can1.create_text(0,ligne*15, text="Début du protocole de communication.",anchor=tkinter.NW)
		ligne=ligne+1
		ligne=ligne+1

	can1.create_text(0,ligne*15-15, text=list_action[etape],anchor=tkinter.NW)
	
	if etape==0:
		affiche_Liste_Clef(l,"orange")
		text8.delete(0.0,tkinter.END)

		
	if etape==1:
		affiche_Liste_Filtre(l,"orange")

	if etape==2:
		affiche_Liste_Photon(l,"orange")

	if etape==3:
		affiche_Liste_Filtre(l,"blue")

	if etape==4:
		affiche_Liste_Photon(l,"blue")

	if etape==5:
		affiche_Liste_Filtre(l,"blue")
	
	if etape==6:
		affiche_Liste_Filtre(l,"orange")

	if etape==7:
		affiche_Liste_Clef(l,"blue")
		
	if etape==8:
		erreur= comparaison_Clef_Finale(clef_alice,clef_bob)
		if erreur:couleur="red"
		else:couleur="green"
		affiche_Liste_Clef(l,couleur)
		
	if etape==9:
		affiche_Liste_Clef(l,"black")
		ligne=ligne+1
		can1.create_text(0,ligne*15, text="Fin du protocole de communication.",anchor=tkinter.NW)
		ligne=ligne+1
		ligne=ligne+1

	ligne=ligne+1

	
# donnée
# une liste l d'entiers compris entre 1 et 4

# résultat
# affiche la représentation d'un photon

def affiche_Liste_Photon(l,couleur):
	global ligne
	for i in range(0,len(l)):
		x1,y1,x2,y2=affiche_Photon(l[i],ligne,i)
		can2.create_line(x1,y1,x2,y2, fill=couleur,width=2)
		
# donnée
# une liste l d'entiers compris entre 0 et 1

# résultat
# affiche la représentation d'un filtre

def affiche_Liste_Filtre(l,couleur):
	global ligne
	for i in range(0,len(l)):
		xa1,ya1,xa2,ya2,xb1,yb1,xb2,yb2=affiche_Filtre(l[i],ligne,i)
		can2.create_line(xa1,ya1,xa2,ya2, fill=couleur,width=2)
		can2.create_line(xb1,yb1,xb2,yb2, fill=couleur,width=2)
		
# donnée
# une liste l d'entiers compris entre 0 et 1

# résultat
# affiche la représentation d'une suite binaire
		
def affiche_Liste_Clef(l,couleur):
	global ligne
	for i in range(0,len(l)):
		x1,y1=affiche_Clef(l[i],ligne,i)
		if l[i]==1:can2.create_text(x1,y1, text="1",anchor=tkinter.NW,fill=couleur)
		if l[i]==0:can2.create_text(x1,y1, text="0",anchor=tkinter.NW,fill=couleur)

# donnée	

# résultat
#affecte la variable réconciliation
def activite_Reconciliation():	
	global reconciliation
	if num_reconciliation==1:reconciliation=1
	if num_reconciliation==3:reconciliation=3

		
# donnée	

# résultat
#affecte la variable pirate

def activite_Pirate():	
	global pirate
	if pirate:
		pirate=False
	else:
		pirate=True

# donnée

# résultat
# affiche la présence d'un pirate sur la ligne

def affiche_Piratage():	
	global ligne
	global etape
	can1.create_text(0,ligne*15, text="   Piratage détecté.",anchor=tkinter.NW,fill="red")
	ligne=ligne+1
	can1.create_text(0,ligne*15, text="Fin de la communication.",anchor=tkinter.NW,fill="red")
	ligne=ligne+1
	ligne=ligne+1
	ligne=ligne+1
	
# donnée

# résultat
# gère le problème!
def phase_Communication():	
	global etape
	global nombre_photon
	global photon_bob
	global photon_alice
	global filtre_bob
	global filtre_alice
	global clef_alice
	global clef_bob
	global reconciliation
	global pirate
	global erreur
	global compteur
	l=[]

	if etape==0:
		#clef_alice=qu_Bit(photon_alice)
		nombre_photon=nombre_photon_emis.get()
		clef_alice=generation_Clef(nombre_photon)
		l=clef_alice
				
	if etape==1:
		filtre_alice=generation_Filtre(len(clef_alice))
		l=filtre_alice
		
	if etape==2:
		photon_alice=generation_Photon_Alice(filtre_alice,clef_alice) 
		
		l=photon_alice

	if etape==3:
		filtre_bob=generation_Filtre(len(clef_alice))
		
		l=filtre_bob
		
	if etape==4:
		nb_bruit=int(nombre_photon*(bruit.get()/100))
		nb_perte=int(nombre_photon*(perte.get()/100))
		photon_bob=photon_Transmission(photon_alice,nb_bruit,nb_perte,filtre_alice,filtre_bob)	
				
		l=photon_bob
		
	if etape==5:		
		photon_alice,photon_bob,filtre_alice,filtre_bob=photon_Manquant(photon_alice,photon_bob,filtre_alice,filtre_bob)
		l=filtre_bob
		

	if etape==6:
		photon_alice,photon_bob,filtre_alice,filtre_bob=filtre_Comparaison(photon_alice,photon_bob,filtre_alice,filtre_bob)
		
		l=filtre_bob
		
	if etape==7:
		if pirate:
			photon_bob=piratage(photon_bob,int(nombre_photon*0.1))
		clef_bob=qu_Bit(photon_bob)
		clef_alice=qu_Bit(photon_alice)
		bloc_connu_alice=bloc_Connu(clef_alice)
		bloc_connu_bob=bloc_Connu(clef_bob)
		l=bloc_connu_bob
		clef_alice=sup_Bloc_Connu(clef_alice)
		clef_bob=sup_Bloc_Connu(clef_bob)
		
		
		nb=int(2.5/100*nombre_photon*10/100)
		bloc_connu_alice_photon=bloc_Connu(photon_alice)
		bloc_connu_bob_photon=bloc_Connu(photon_bob)
		if detection_Pirate(bloc_connu_alice_photon,bloc_connu_bob_photon,nb):
				affiche_Piratage()
				etape=10
			
		#if num_reconciliation.get()==0:
			#Sans réconciliation bob ne peut pas savoir si sa clef est correcte
			
		if reconciliation==1:
			
			clef_bob=reconciliation_Parite_Simple(clef_alice,clef_bob)
			list_erreur=comparaison_Clef(clef_alice,clef_bob)
			affiche_Reconciliation(list_erreur,clef_bob)
			
		if reconciliation==3:
			clef_bob=reconciliation_Parite_Hamming(clef_alice,clef_bob)
			list_erreur=comparaison_Clef(clef_alice,clef_bob)
			affiche_Reconciliation(list_erreur,clef_bob)
		

	if etape==8:
		l=clef_bob
		
	if etape==9:
		clef_amplifie=amplification_Clef(clef_bob)
		l=clef_amplifie
		r=taux_De_Transfert(len(clef_amplifie),nombre_photon)
		text8.delete(0.0,tkinter.END)
		text8.insert(0.0,r)

	if etape<10:
		affiche_Etape(l)
	else: 
		etape=-1
		compteur=compteur+1
		
	etape=etape+1
		
reglage=tkinter.Tk()
reglage.title("Paramêtres")
reglage.geometry("400x260+100+0")

text0 = tkinter.Label(reglage, text='Photon émis', fg='blue')
text0.grid(row =0, column=0,padx =3, pady =3)
nombre_photon_emis=tkinter.IntVar() # prevoir la variable pour recevoir le texte saisi
ent=tkinter.Entry(textvariable=nombre_photon_emis,width=30,foreground="blue",background="lightgray")
ent.grid(row =0, column=1,padx =3, pady =3)
ent.delete(0,tkinter.END)
ent.insert(0, "500")

label1 =tkinter.Label(reglage, text='Bruit de la ligne', fg='blue')
label1.grid(row =1, column=0,padx =3, pady =3)
label2 = tkinter.Label(reglage, text='%', fg='blue')
label2.grid(row =1, column=2,padx =3, pady =3)

bruit=tkinter.DoubleVar() # prevoir la variable pour recevoir le texte saisi
ent1=tkinter.Entry(textvariable=bruit,width=30,foreground="blue",background="lightgray")
ent1.delete(0,tkinter.END)
ent1.insert(0, "0.5")
ent1.grid(row =1, column=1,padx =3, pady =3)

label3 = tkinter.Label(reglage, text='perte en ligne', fg='blue')
label3.grid(row =2, column=0,padx =3, pady =3)
label4 = tkinter.Label(reglage, text='%', fg='blue')
label4.grid(row =2, column=2,padx =3, pady =3)

perte=tkinter.DoubleVar() # prevoir la variable pour recevoir le texte saisi
ent2=tkinter.Entry(textvariable=perte,width=30,foreground="blue",background="lightgray")
ent2.delete(0,tkinter.END)
ent2.insert(0, "3")
ent2.grid(row =2, column=1,padx =3, pady =3)

val=tkinter.IntVar()
chk=tkinter.Checkbutton(reglage, variable=val, text="Piratage",command=activite_Pirate)
chk.grid(row =3, column=1,padx =3, pady =3)

text5 = tkinter.Label(reglage, text='Réconciliation', fg='blue')
text5.grid(row =4, column=0,padx =3, pady =3)

num_reconciliation=tkinter.IntVar()
tkinter.Radiobutton (reglage, variable=num_reconciliation, text="Pas de réconciliation",value=0,anchor=tkinter.W,command=activite_Reconciliation).grid(row =4, column=1,padx =3, pady =3)
tkinter.Radiobutton (reglage, variable=num_reconciliation, text="Protocole cascade",value=1,anchor=tkinter.W,command=activite_Reconciliation).grid(row =5, column=1,padx =3, pady =3)
#tkinter.Radiobutton (reglage, variable=num_reconciliation, text="Code à répétition",value=2,anchor=tkinter.W,command=activite_reconciliation).grid(row =5, column=1,padx =3, pady =3)
tkinter.Radiobutton (reglage, variable=num_reconciliation, text="Protocole Winnow",value=3,anchor=tkinter.W,command=activite_Reconciliation).grid(row =6, column=1,padx =3, pady =3)
num_reconciliation.set(0)  # initialisation du choix parité simple

#text6 = tkinter.Label(reglage, text='Amplification de confidentialité', fg='blue')
#text6.grid(row =7, column=0,padx =3, pady =3)

text7 = tkinter.Label(reglage, text='Transfert', fg='blue')
text7.grid(row =8, column=0,padx =3, pady =3)

text8=tkinter.Text(reglage,width=10,height=1,bg='gray', fg='purple',font=("Helvetica",15))
text8.grid(row =8, column=1,padx =3, pady =3)

text9 = tkinter.Label(reglage, text='%', fg='gray')
text9.grid(row =8, column=2,padx =3, pady =3)

bouton = tkinter.Button(reglage, text='Phase suivante', command=phase_Communication)
bouton.grid(row =9, column=1,padx =3, pady =3)

racine = tkinter.Tk()
racine.title("Trace du protocole BB84")

racine.geometry("1000x500+100+300")

s3 = tkinter.Scrollbar(racine)
s4 = tkinter.Scrollbar(racine)
s5 = tkinter.Scrollbar(racine,orient=tkinter.HORIZONTAL)

s3.pack(side=tkinter.LEFT, fill=tkinter.Y)

can1 = tkinter.Canvas(racine, width=300, height=100,scrollregion=(0,0,2000,2000))
can1.pack(side=tkinter.LEFT, fill=tkinter.Y)

s3.config(command=can1.yview)
can1.config(yscrollcommand = s3.set)

s4.pack(side=tkinter.LEFT, fill=tkinter.Y)
s5.pack(side=tkinter.BOTTOM, fill=tkinter.X)
largeur=int(nombre_photon*3)
can2 = tkinter.Canvas(racine, width=200, height=100,scrollregion=(0,0,12*2000,20000))
can2.pack(side=tkinter.LEFT, fill=tkinter.Y)

s4.config(command=can2.yview)
s5.config(command=can2.xview)
can2.config(yscrollcommand = s4.set, xscrollcommand = s5.set)

racine.mainloop()
reglage.mainloop()
