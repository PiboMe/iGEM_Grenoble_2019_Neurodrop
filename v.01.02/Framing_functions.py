#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:55:48 2019

@author: pierrebouvet
"""

from tkinter import Label,Button,Frame,Canvas
from PIL import Image, ImageTk
#from functools import partial
#import funct_fenetre_principale as ffp


def Create_Frame(Window, border_thickness=5, style_border='raised', back_colour='', col=0, line=0, nblines=1, nbcolumns=1, form='wens'):
    """
    This function creates a frame with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        border_thickness(int): the thickness of the border
        style_border(str): the type of the border
        back_colour(str): the background of the frame
        col(int): the column of the frame
        line(int): the line of the frame
        nblines(int): the number of lines on which the frame is (>0)
        nbcolumns(int): the number of columns on which the frame is (>0)
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
    Returns:
        The frame with all of the parameters stated above
    
    Nota: Parameters are by default the ones of the head of the window
    """
    #Either use raised as relief or "groove"
    #Use hexadecimal values to define the background, here the color is blue
    Frame_created=Frame(Window, bd=border_thickness, relief=style_border, background=back_colour)
    Frame_created.grid(column=col, row=line, columnspan=nbcolumns, rowspan=nblines, sticky=form)
    return Frame_created

def Create_text(Window, Text, color='#e7feff', Police='Baskerville 45 italic', back_colour="#318ce7", col=0, line=0, form='wens'):
    """
    This function creates a text label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        Text(str): the text of the label
        color(str): the color of the text (we recommend hexadecimal notation)
        Police(str): the font of the text
        back_colour(str): the background of the text (we recomment hexadecimal notations)
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    #The parameters correspon to the Neurodrop fonts and backgrounds
    Label_text=Label(Window,text=Text,foreground=color,font=Police,background=back_colour)    
    Label_text.grid(column=col,row=line,sticky=form)
    return Label_text

def Create_button(Window, Text, Function, color='#000000', activefg='#318ce7', Width=30, Height=2, Police='Arial 25', col=0, line=0, form='wens'):
    """
    This function creates a button label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        Text(str): the text of the label
        activefg(str): the color of the text when pressed
        Width(int): the width of the button
        Height(int): the height of the button
        Police(str): the font of the text
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
        Function(function): the fuction that, when the button is pressed, is started (we recommend to use a function that is then included with 'partial')
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    Label_button=Button(Window, text=Text, foreground=color, activeforeground=activefg, width=Width, height=Height, font=Police, command=Function)
    Label_button.grid(column=col,row=line,sticky=form)
    return Label_button


def Create_Image(Window, file, finalmaxwidth=300, finalmaxheight=500, col=0, line=0, form='wens'):
    """
    This function creates a button label with the tkinter library
    
    Entry:
        Window(Frame): the parent frame
        file(str): the path of the image file
        finalmaxwidth(int): the maximal width the image can have
        finalmaxheight(int): the maximal height the image can have
        col(int): the column at which the button is
        line(int): th row at which the button is
        form(str): the sticky parameter (a string containing some or all of the letters w,e,n,s)
    Returns:
        The label with all of the parameters stated above
    
    Nota: Parameters are by default the ones of Neurodrop
    """
    img= Image.open(file)
    sze=img.size
    if (sze[0]/finalmaxwidth > sze[1]/finalmaxheight):
        w=sze[1]/finalmaxheight
    else:
        w=sze[0]/finalmaxwidth
    img=img.resize((int(w*finalmaxwidth), int(w*finalmaxheight)),Image.ANTIALIAS)
    Label_image=Canvas(Window, width=w*finalmaxwidth, height=w*finalmaxheight)
    Label_image.create_image(int(w*finalmaxwidth/2), int(w*finalmaxheight/2),image=img)
    Label_image.grid(column=col,row=line, sticky=form)
    return Label_image


def Auto_configure_rows_columns_Frames(Window, lines=[], columns=[], min_size_row=30, min_size_col=30,weight_col=1,weight_row=1):
    """
    This function configures a frame with the tkinter library
    
    Entry:
        Window(Frame): the fram to configure
        lines(list): the list of rows we want to apply the algorithm to
        columns(list): the list of columns we want to apply the algorithm to
        min_size_row(int): the minimal size of the rows in pixels
        min_size_col(int): the minimal size of the columns in pixels
        weight_col(int): the weight of the columns when we resize the window
        weight_row(int): the weight of the lines when we resize the window
    Returns:
        The frame well configurated
    """
    for r in lines:
        for c in columns:
            Window.columnconfigure(c,min_size_col,weight=weight_col)
            Window.rowconfigure(r,min_size_row,weight=weight_row)
    return 1


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    