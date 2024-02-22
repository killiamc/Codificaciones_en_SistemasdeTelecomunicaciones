from distutils.cmd import Command
from logging import root
from operator import le
from pickle import FRAME
from pydoc import describe 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from traceback import FrameSummary
from turtle import color, fd
import math 
import numpy as np
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import RLE as rle
import Huffman as hufman
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica
import pantalla_inicio as inicio

class Interfaz_lineal():
    def __init__(self,root):
        self.root = root
        self.frase = StringVar()
        self.seleccionTec = IntVar()
        self.mat = []
        pass

    def creador(self):
        messagebox.showinfo("Autores","Daniela Sosa Y Killiam Puentes")

    def nrz(self,bits):
        for i in bits:
            if i == "1" or i=="0":
                ver = True
            else:
                ver = False
        if ver:
            paso = len(bits)
            datos = 20
            y = []
            for i in bits:
                if i == "1":
                    x = np.full(datos, 1)
                elif i == "0":
                    x = np.full(datos, 0)
                b = list(x)
                for i in range(len(b)):
                    y.append(b[i])
            t = np.arange(0,paso,1/datos)
            y = np.array(y)
            self.pantalla_final(t,y,bits)
        else :
            messagebox.showwarning("Lineal","Ingrese de nuevo el solo se aceptan bits")
            self.frase.set("")

    def pseudo_ternario(self,bits):
        for i in bits:
            if i == "1" or i=="0":
                ver = True
            else:
                ver = False
        if ver:
            paso = len(bits)
            datos = 20
            y = []
            v = random.randrange(2,5,2)-3
            estado_anterior = str(v)
            for i in bits:
                if i == "1":
                    x = np.full(datos, 0)
                elif i == "0":
                    if estado_anterior == "1":
                        x = np.full(datos, 1)
                        estado_anterior = "-1"
                    elif estado_anterior == "-1":
                        x = np.full(datos, -1*1)       
                        estado_anterior = "1" 
                b = list(x)
                for i in range(len(b)):
                    y.append(b[i])                  
            t = np.arange(0,paso,1/datos)
            y = np.array(y)
            self.pantalla_final(t,y,bits)
        else :
            messagebox.showwarning("Lineal","Ingrese de nuevo el solo se aceptan bits")
            self.frase.set("")

    def CMI(self,bits):
        for i in bits:
            if i == "1" or i=="0":
                ver = True
            else:
                ver = False
        if ver:
            paso = len(bits)
            datos = 20
            y = []
            v = random.randrange(2,5,2)-3
            estado_anterior = str(v)
            for i in bits:
                if i == "1":
                    if estado_anterior == "1":
                        x = np.full(datos, -1)
                        estado_anterior = "-1"
                    elif estado_anterior == "-1":
                        x = np.full(datos, 1)       
                        estado_anterior = "1" 
                    b = list(x)
                elif i == "0":
                    x = []
                    for i in range(datos):
                        if i < round(datos/2):
                            x.append(-1)
                        else:
                            x.append(1)
                    b =x
                for i in range(len(b)):
                    y.append(b[i])                  
            t = np.arange(0,paso,1/datos)
            y = np.array(y)
            self.pantalla_final(t,y,bits)
        else :
            messagebox.showwarning("Lineal","Ingrese de nuevo el solo se aceptan bits")
            self.frase.set("")
        

    def pantalla_final(self,t,y,bits):
        self.frmlineal.destroy()
        self.frmfinal = Frame()
        self.frmfinal.pack()
        self.frmfinal.config(width="400",height="260",background="light steel blue",bd=10,relief="raised")
        
        fig = Figure(figsize=(3,3),dpi=150)
        # fig, ax = plt.subplots(figsize=(1,1),dpi=100)   
        co = "c"
        t = [0, 5, 5.1,6,7,8,9,10,11,15]
        y = [6, 10,10.2,12,14,16 ,18,20,30,14]
        t1 = [5,6,7,8,9,10,11,12]
        y1 = [15,15,15,15,15,15,15,15]
        y2 = [-15,-15,-15,-15,-15,-15,-15,-15]
        fig.add_subplot(111).plot(t,y,'r',t1,y1,'b',t1,y2,'b')

        posf = 0
        posc = 0
        lblin = ttk.Label(self.frmfinal,text="Codificacion",font=(48),foreground="Darkorange1",justify=CENTER)
        lblin.config(background="light steel blue")
        lblin.grid(row=posf,column=posc,columnspan=2)

        posf += 1
        posc += 1
        mensajetxt = Text(self.frmfinal,width=30, height=10,font=("consolas",12),background="lightcyan")
        mensajetxt.insert('1.0',bits)
        mensajetxt.grid(row=posf,column=posc,padx=8)
        
        posc += 1
        canvas = FigureCanvasTkAgg(fig,master=self.frmfinal)
        canvas.draw()
        canvas.get_tk_widget().grid(row=posf,column=posc)
        
        posf+=1
        btnmodifi = ttk.Button(self.frmfinal,text="Volver",style="MyButton.TButton",
            command=lambda:[self.frmfinal.destroy(),self.pantalla_lineal()])
        btnmodifi.grid(row=posf,column=posc)


    def opcion(self,bits):
        if self.seleccionTec.get() == 1:
            self.nrz(bits)
        elif self.seleccionTec.get() == 2:
            self.pseudo_ternario(bits)
        elif self.seleccionTec.get() == 3:
            self.CMI(bits)
        else:
            messagebox.showwarning("Lineal","Ingrese la codificación lineal")
        
    def pantalla_lineal(self):
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="orangered4",
        )
        self.frmlineal = Frame()
        self.frmlineal.pack()
        
        self.frmlineal.config(width="400",height="260",background="light steel blue",bd=10,relief="raised")

        posf = 0
        posc = 0
        lblin = ttk.Label(self.frmlineal,text="Ingrese la codificación",font=(48),foreground="Darkorange1",justify=CENTER)
        lblin.config(background="light steel blue")
        lblin.grid(row=posf,column=posc,columnspan=2)

        posf += 1
        posc = 0
        frasetxtde = Entry(self.frmlineal,font=("consolas",8),background="lightcyan",fg="Darkorange1",textvariable=self.frase)
        frasetxtde.grid(row=posf,column=posc,columnspan=2,ipady=20) 

        posf += 1
        rbNRZ = Radiobutton(self.frmlineal,background="light steel blue",foreground="purple2",text="NRZ-l",variable=self.seleccionTec,value=1)
        rbNRZ.grid(row=posf,column=posc)

        posf += 1
        rbpse = Radiobutton(self.frmlineal,background="light steel blue",foreground="purple2",text="Pseudo Ternario",variable=self.seleccionTec,value=2)
        rbpse.grid(row=posf,column=posc)
        posc = 1
        btnmodifi = ttk.Button(self.frmlineal,text="graficar",style="MyButton.TButton",
            command=lambda:[self.opcion(self.frase.get())])
        btnmodifi.grid(row=posf,column=posc)

        posc = 0
        posf += 1
        rbman = Radiobutton(self.frmlineal,background="light steel blue",foreground="purple2",text="CMI",variable=self.seleccionTec,value=3)
        rbman.grid(row=posf,column=posc)



class principal_Lineal():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificaciones Lineales")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_lineal.creador(self))
        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="Huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Aritmetica",command=lambda:[root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
        Canal.add_command(label="Algebraica",command=lambda:[root.destroy(),algebraica.principal_Algebraica.iniciar(self)])
                
        rLe = Menu(barra_menu,tearoff=0)
        rLe.add_command(label="RLE",command=lambda:[root.destroy(),rle.principal_RLE.iniciar(self)])

        barra_menu.add_cascade(label="inicio",menu=Inicio)
        barra_menu.add_cascade(label="Cod.Canal",menu=Canal)
        barra_menu.add_cascade(label="RLE",menu=rLe)
        barra_menu.add_cascade(label="Ayuda",menu=ayudatr)

        s1 = Interfaz_lineal(root)
        s1.pantalla_lineal()
        root.mainloop()

x = principal_Lineal()
x.iniciar()