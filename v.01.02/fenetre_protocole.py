#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:23:43 2019

@author: pierrebouvet
"""

from tkinter import Label,Button,Frame
from functools import partial
import funct_fenetre_protocole as ffp                     

global globalprotocole
    
def Affichage_commandes(fenetre):
    protocole=globalprotocole
    #On cree la Frame commande
    Commande=Frame(fenetre,bd=5,relief='groove')
    #On cree le label du texte
    text_Command=Label(Commande,text='Commands', background="#87cefa",font="Arial 30")
    #On cree les boutons
    bouton_Pipeter=Button(Commande,text='Pipet solution', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.Pipeter, fenetre, protocole))
    bouton_DeposerEWOD=Button(Commande,text='Drop on EWOD', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.DeposeEWOD, fenetre, protocole))
    bouton_DeplacerGoutte=Button(Commande,text='Move drop', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.DeplacerGoutte, fenetre, protocole))
    bouton_MesurLumine=Button(Commande,text='Measure Luminescence', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.MeasureLum, fenetre, protocole))
    bouton_Assainir=Button(Commande,text='Clean EWOD surface', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.Clean, fenetre, protocole))
    bouton_Decongeler=Button(Commande,text='Thaw solutions', activeforeground='#318ce7',width=30,font="Arial 25",command=partial(ffp.Thaw, fenetre, protocole))
    #On positionne les boutons
    text_Command.grid(column=1,row=1,sticky='wens')
    bouton_Pipeter.grid(column=1,row=2, sticky='wens')      
    bouton_DeposerEWOD.grid(column=1,row=3,sticky='wens')
    bouton_DeplacerGoutte.grid(column=1,row=4,sticky='wens')
    bouton_MesurLumine.grid(column=1,row=5,sticky='wens')
    bouton_Assainir.grid(column=1,row=6,sticky='wens')  
    bouton_Decongeler.grid(column=1,row=7,sticky='wens')            
                              
def Protocole(fenetre,file_protocole=''):
    protocole=globalprotocole
    ffp.Affichage_bandeau(fenetre)
    protocole=[]
    if len(file_protocole)==0:
        #Donc on crée un nouvea protocole à partir de 0
        Affichage_commandes(fenetre)
    else:
        #Il faut déjà afficher le protocole actuel
        protocole=ffp.Affichage_protocole_fichier(file_protocole)
    ffp.Apparence_fenetre(fenetre)
    return protocole
