#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:50:05 2019

@author: pierrebouvet
"""

from tkinter import Frame, Label

def Affichage_bandeau(fenetre):
    #On cree la Frame bandeau
    Bandeau=Frame(fenetre,bd=5,relief='raised')
    #On ajoute les noms
    Label_text_Neurodrop=Label(Bandeau,text='Neurodrop',foreground='#e7feff',font="Baskerville 45 italic", background='#318ce7')
    Label_text_iGEM=Label(Bandeau,text='iGEM Grenoble 2019',background='#006b3c',font="Arial 30 bold", foreground='#ffffff')
    Label_text_version=Label(Bandeau,text='version 01.000',background='#ffdead',font="Baskerville 12 italic",foreground='#191970')                
    #On positionne les noms
    Label_text_Neurodrop.grid(column=0,row=0, sticky='wens')
    Label_text_iGEM.grid(column=1,row=0, sticky='wens')
    Label_text_version.grid(column=2,row=0, sticky='wens') 
    #On définit l'apparence du bandeau
    Bandeau.columnconfigure(0,weight=1)
    Bandeau.columnconfigure(1,weight=1)
    Bandeau.columnconfigure(2,weight=1)  
    
def Apparence_fenetre(fenetre):
    fenetre.columnconfigure(0,minsize=500,weight=1)
    fenetre.columnconfigure(1,minsize=500,weight=1)

def Affichage_protocole_fichier(file):
    #Ici on ouvre le fichier et on 
    return 0

def Pipeter(fenetre,protocole):
    #Ouvrir une nouvelle fenetre avec quelle solution pipeter et combien pipeter
    vol=20 #volume en microlitre
    sol=1 #solution
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['pip',vol,sol])
    protocole=a+b
    return protocole

def DeplacerGoutte(fenetre,protocole):
    #Ouvrir une fenêtre pour définir le pad de départ et le pad de fin
    xbeg=0
    ybeg=0
    xend=0
    yend=0
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['mov',xbeg,ybeg,xend,yend])
    protocole=a+b
    return protocole

def MeasureLum(fenetre,protocole):
    #Ouvrir une fenêtre pour définir le nombre de mesures à faire avant de renvoyer le résultat moyenné
    nmes=100
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['lum',nmes])
    protocole=a+b
    return protocole

def DeposeEWOD(fenetre,protocole):
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['dep'])
    protocole=a+b
    return protocole

def Clean(fenetre,protocole):
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['ass'])
    protocole=a+b
    return protocole

def Thaw(fenetre,protocole):
    i=protocole.index('position')
    a=protocole[:i]
    b=protocole[i:]
    a.append(['dec'])
    protocole=a+b
    return protocole