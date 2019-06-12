#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:28:27 2019

@author: pierrebouvet
"""

from tkinter import Tk,Canvas
from functools import partial
from Framing_functions import Create_Frame, Create_text, Create_button, Create_Image
import funct_fenetre_principale as ffp


# =============================================================================
# Initialisation de la fenetre
# =============================================================================

Window_main=Tk()
Window_main.title('Neurodrop - Main window')

# =============================================================================
# Infos & Styles
# =============================================================================

# Infos
nb_version='01.02'

# Style couleurs

    #Background colors
    
Bkg_txt_Neuro='#318ce7'
Bkg_txt_iGEM='#006b3c'
Bkg_txt_vers='#ffdead'

Bkg_frm_blue='#87cefa'
Bkg_frm_white='#ffffff'

Bkg_button_active='#318ce7'

    #Text colors

Clr_txt_Neuro='#e7feff'
Clr_txt_iGEM='#ffffff'
Clr_txt_vers='#191970'

Clr_txt_frames='#004b49'

Clr_txt_begin="#00fa9a"

#Styles ecritures

Font_iGEM='Arial 30 bold'
Font_vers='Baskerville 12 italic'

Font_frames_title='Arial 30'
Font_frames_begin='Arial 25 bold'


# =============================================================================
# Creation of the labels (nomenclature: Type_name)
# =============================================================================

#Groupes
Bandeau=Create_Frame(Window_main, nbcolumns=2)
Protocol=Create_Frame(Window_main, style_border='groove', back_colour=Bkg_frm_blue, line=2, form='')
Measure=Create_Frame(Window_main, style_border='groove', back_colour=Bkg_frm_blue, line=4, form='')
ImageZone=Create_Frame(Window_main, style_border='groove', back_colour=Bkg_frm_white, col=1, line=2, nblines=3, nbcolumns=2)

#Label texte
Text_Neurodrop=Create_text(Window_main, 'Neurodrop')
Text_iGEM=Create_text(Window_main, 'iGEM Grenoble 2019',color=Clr_txt_iGEM, Police=Font_iGEM, back_colour=Bkg_txt_iGEM, col=1, line=0, form='wens')
Text_version=Create_text(Window_main, 'version '+nb_version,color=Clr_txt_vers, Police=Font_vers, back_colour=Bkg_txt_vers, col=2)
Text_MeasureProtocol=Create_text(Protocol, 'Measurement Protocol:',color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue,col=1,line=1)
Text_MakeMeasurement=Create_text(Measure, 'Apply protocol',color=Clr_txt_frames, Police=Font_frames_title, back_colour=Bkg_frm_blue,col=1,line=1)
                         
#Label boutons
Button_CreateNewProtocol=Create_button(Protocol, 'Create a new protocol', partial(ffp.CreateNewProtocol, Window_main), activefg=Bkg_button_active, col=1, line=2, form='wens')
Button_OpenMeasureProtocol=Create_button(Protocol, 'Load an existing protocol', partial(ffp.OpenMeasureProtocol, Window_main), activefg=Bkg_button_active, col=1, line=3, form='wens')
Button_ModifyProtocol=Create_button(Protocol, 'Modify an existing protocol', partial(ffp.ModifyProtocol, Window_main), activefg=Bkg_button_active, col=1, line=4, form='wens')
Button_BeginMeasurement=Create_button(Measure, 'Begin Measure', partial(ffp.BeginMeasurement, Window_main), activefg=Bkg_button_active, col=1, line=2, form='wens',color=Clr_txt_begin, Police=Font_frames_begin)      
   
#Label Image

#image=PhotoImage(file="Logo_vectorisé.png")
zone_image=Create_Image(ImageZone, 'Logo.png', finalmaxwidth=200, finalmaxheight=200, col=0, line=0, form='wens')


# =============================================================================
# Réglage des cellules de la grille
# =============================================================================

#Column
Window_main.columnconfigure(0,minsize=500,weight=1)
Window_main.columnconfigure(1,minsize=500,weight=1)
Bandeau.columnconfigure(0,weight=1)
Bandeau.columnconfigure(1,weight=1)
Bandeau.columnconfigure(2,weight=1)
Protocol.columnconfigure(0,minsize=10)
Protocol.columnconfigure(2,minsize=10)
Measure.columnconfigure(0,minsize=10)
Measure.columnconfigure(2,minsize=10)

#Rows
Window_main.rowconfigure(1,minsize=40)
Window_main.rowconfigure(2,minsize=40,weight=1)
Window_main.rowconfigure(3,minsize=40)
Window_main.rowconfigure(4,minsize=40,weight=1)
Window_main.rowconfigure(5,minsize=40)
Bandeau.rowconfigure(0,weight=1)
Protocol.rowconfigure(0,minsize=10,weight=1)
Protocol.rowconfigure(5,minsize=10,weight=1)
Measure.rowconfigure(0,minsize=10,weight=1)
Measure.rowconfigure(3,minsize=10,weight=1)



Window_main.mainloop()

