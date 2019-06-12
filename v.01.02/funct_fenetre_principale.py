#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:22:45 2019

@author: pierrebouvet
"""

from tkinter import Toplevel
import fenetre_protocole as fp

def update_label(label,new_text):
    #Modifie le texte d'un label
    label.config(text=new_text)

def CreateNewProtocol(fenetre_depart):
    #Ouvre la fenêtre de création du fichier et renvoie une liste de commande
    print("Ici on doit ouvrir une nouvelle fenêtre, permettre de créer le protocole, l'enregistrer, et le retourner sous forme de liste")
    fen_protocole=Toplevel(fenetre_depart)
    fen_protocole.title('Neurodrop - New Protocol')
    fen_protocole.transient(fenetre_depart)
    list_command=fp.Protocole(fen_protocole)
    return list_command

def OpenMeasureProtocol(fenetre_depart):
    print("Ici on ouvre un protocole déjà créé et on le renvoie sous forme de liste")
    list_command=[]
    return list_command

def ModifyProtocol(fenetre_depart):
    print("Ici on ouvre un fichier existant, on l'ouvre dans le modificateur, on l'enregistre et on le renvoie sous forme de liste")
    list_command=[]
    return list_command

def BeginMeasurement(fenetre_depart):
    print("Ici on commence la mesure, on ouvre une nouvelle fenêtre avec l'avancement")