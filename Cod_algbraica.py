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

import Hamming as hamm
import Huffman as hufman
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import pantalla_inicio as inicio
import Lineal as ln
import RLE as rle

class Cod_algebraica():
    def __init__(self,matriz,fr):
        self.mat_alge = matriz
        self.frase = fr
        self.L = 0

    def num_bas(self):
        num = "0."
        for i in self.frase:
            for j in range(len(self.mat_alge)):
               if i == self.mat_alge[j][0]:
                n = str(self.mat_alge[j][1])
                num += n
        fin = len(self.mat_alge)
        bas = self.mat_alge[fin-1][1]+1
        self.L =len(self.frase)
        return num,bas
    
    def decimal(self):
        num,bas = self.num_bas()
        dec = 0
        for i in range(self.L):
            n = pow(bas,-(i+1))
            n1 = int(num[2+i])
            s = n*n1
            dec += s 
            dec = round(dec,10)
        return dec,num,bas

    def deci2(self,bits):
        decim = 0
        for i in range(len(bits)):
            n = pow(2,-(i+1))
            b = int(bits[i])
            s = n*b
            decim += s
        return decim

    def base(self,decimal,b):
        base = ""
        decimal = round(decimal,8)
        for i in range(self.L):
            nuevo = decimal*b
            if i == self.L-1:
                en = math.ceil(nuevo)
                n = str(en)
                op1 = str(nuevo)
                op2 = n
            else:
                if nuevo >= 1:
                    en = int(nuevo // 1)
                    n = str(en)
                else:
                    en = 0
                    n = str(en)
                decimal = nuevo - en
            base += n
        base = "0."+base
        return base,op1,op2

    def binario(self):
        dec,num,bas = self.decimal()
        decim =dec
        acabar = True
        f_bits = ""
        while acabar:
            n_dec = decim*2
            if n_dec >= 1:
                en = n_dec // 1
                b = "1"
            else:
                en = 0
                b="0"
            f_bits += b
            if b == "1":
                dec_prueba = self.deci2(f_bits) #se hace dec prueba la cual pasa a decimal si ahi un 1
                base,op1,op2 = self.base(dec_prueba,bas)
                if base == num:
                    acabar = False
            decim = n_dec-en
        f_bits = "0."+f_bits
        dec = str(dec)
        dec_prueba=str(dec_prueba)
        b = str(bas)
        return f_bits,base,dec_prueba,dec,self.L,op1,op2,b
            

class Interfaz_Algebraica():
    def __init__(self,root):
        self.root = root
        self.frmAlgebraica = Frame()
        self.frase = StringVar()
        self.conta = 0
        self.unicos = []
        pass
    
    def creador(self):
        messagebox.showinfo("Autores","Daniela Sosa Y Killiam Puentes")

    def limpiar(self):
        limpiar = " "
        self.frase.set(limpiar)

    def pantalla_resultado(self,frase,redun):
        self.frmresultado = Frame()
        fr = frase.get()
        frase_nueva = ""
        for i in fr:
            if i != " ":
                frase_nueva += i 
        if len(frase_nueva)<=20 and len(frase_nueva)>2 :
            if redun == "1":
                self.conta=0
                self.unicos = []
                for i in frase_nueva:
                        vera = True
                        momento = []
                        for j in fr:
                            if i == j:
                                if vera:
                                    if i == " ":
                                        i = "esp"
                                        momento.append(i)
                                        vera = False
                                    else:
                                        momento.append(i)
                                        vera = False
                        if len(self.unicos) == 0:
                            self.unicos.append(momento)
                        elif len(self.unicos) > 0:
                            vera = True
                            for k in range(len(self.unicos)):
                                if self.unicos[k][0] == i:
                                    vera = False
                            if vera:
                                self.unicos.append(momento)

            #segunda condicion

            if len(self.unicos)>=3 and len(self.unicos)<=9:
                self.frmresultado.pack()
                self.frmAlgebraica.forget()
                print(self.unicos)
                for i in range(len(self.unicos)):
                    self.unicos[i].append(i)
                print(self.unicos)
                algebraica= Cod_algebraica(self.unicos,frase_nueva)
                bits,numbase,dec2,decori,l,op1,op2,b = algebraica.binario() 
                #------------------------------------------------------------------pantalla resultado
                print(bits)
                self.frmresultado.config(width="400",height="230",background="burlywood1",bd=10,relief="raised")

                lblre = ttk.Label(self.frmresultado,text="Resultado",font=(48),foreground="springgreen4")
                lblre.config(background="burlywood1")
                lblre.grid(row=0,column=0,columnspan=3)

                lblfra = ttk.Label(self.frmresultado,text=fr,justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lblfra.grid(row=1,column=0,columnspan=3)
                
                lblbits = ttk.Label(self.frmresultado,text="# de Bits →",justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lblbits.grid(row=2,column=0)

                resultxt = Text(self.frmresultado,width=20, height=2,font=("consolas",12),background="bisque2")
                resultxt.insert('1.0',bits)
                resultxt.grid(row=2,column=1,columnspan=2)

                lbldec_ori = ttk.Label(self.frmresultado,text="# base 10 original →",justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lbldec_ori.grid(row=3,column=0)

                result10txt = Text(self.frmresultado,width=20, height=2,font=("consolas",12),background="bisque2")
                result10txt.insert('1.0',decori)
                result10txt.grid(row=3,column=1,columnspan=2)

                lbldecn = ttk.Label(self.frmresultado,text="# base 10 redondeado →",justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lbldecn.grid(row=4,column=0)

                result101txt = Text(self.frmresultado,width=20, height=2,font=("consolas",12),background="bisque2")
                result101txt.insert('1.0',dec2)
                result101txt.grid(row=4,column=1,columnspan=2)

                fr = " numero original →"
                lblbase = ttk.Label(self.frmresultado,text=fr,justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lblbase.grid(row=5,column=0)

                resultbstxt = Text(self.frmresultado,width=20, height=2,font=("consolas",12),background="bisque2")
                resultbstxt.insert('1.0',numbase)
                resultbstxt.grid(row=5,column=1,columnspan=2)

                L = "base = "+b+" l = "+str(l)
                lbll = ttk.Label(self.frmresultado,text=L,justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lbll.grid(row=6,column=0)
                
                t = op1+" → "+op2
                lblredo = ttk.Label(self.frmresultado,text=t,justify="center",font=(24),foreground="springgreen4",background="burlywood1")
                lblredo.grid(row=6,column=1,columnspan=2)

                btnregresar = ttk.Button(self.frmresultado,text="regresar",style="MyButton.TButton"
                    ,command=lambda:[self.frmresultado.destroy(),self.pantalla_algebraica()])
                btnregresar.grid(row=7,column=2,columnspan=2)

            else:
                messagebox.showwarning("Codificación Algebraica","El numero de caracteres unicos no es el requerido :/")
                self.frase.set("")
        else:
            messagebox.showwarning("Codificación Aritmetica","La frase es muy larga o no posee nada digite de nuevo :)")
            self.frase.set("")
        
        
#-----------------------------------------------------------------------------pantalla----------------------------------------------------------
    def pantalla_algebraica(self):
        self.unicos = []
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="orangered4",
        )
        s1 = ttk.Style()
        s1.configure(
            "MyButton.TButton",
            foreground="orangered4",
            background="purple1"
        )
        self.frmAlgebraica.pack()
        self.frmAlgebraica.config(width="400",height="230",background="burlywood1",bd=10,relief="raised")

        lbl = ttk.Label(self.frmAlgebraica,text="Ingrese la frase:",font=(48),foreground="springgreen4")
        lbl.config(background="burlywood1")
        lbl.place(x=110,y=10)

        frasetxt = Entry(self.frmAlgebraica,font=("consolas",14),textvariable=self.frase,justify="center",background="bisque2",fg="sienna4")
        # frasetxt = Entry()
        frasetxt.place(x=40,y=50,width=300,height=50)
        fr = frasetxt.get()
        lbl1 = ttk.Label(self.frmAlgebraica,text="Desea ingresar probabilidad",font=(48),foreground="springgreen4")
        lbl1.config(background="burlywood1")
        lbl1.place(x=60,y=120)

        btncalculo = ttk.Button(self.frmAlgebraica,text="Calcular",style="MyButton.TButton"
            ,command=lambda:self.pantalla_resultado(self.frase,"1"))
        btncalculo.place(x=60,y=160)

        btncallimpiar = ttk.Button(self.frmAlgebraica,text="Limpiar",style="MyButtonL.TButton",
            command=lambda:self.limpiar())
        btncallimpiar.place(x=230,y=160)
      

class principal_Algebraica():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificacion Algebraica")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_Algebraica.creador(self))
        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="Huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Aritmetica",command=lambda:[root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
                        
        rLe = Menu(barra_menu,tearoff=0)
        rLe.add_command(label="RLE",command=lambda:[root.destroy(),rle.principal_RLE.iniciar(self)])

        Linear = Menu(barra_menu,tearoff=0)
        Linear.add_command(label="Lineal",command=lambda:[root.destroy(),ln.principal_Lineal.iniciar(self)])

        barra_menu.add_cascade(label="inicio",menu=Inicio)
        barra_menu.add_cascade(label="Cod.Canal",menu=Canal)
        barra_menu.add_cascade(label="RLE",menu=rLe)
        barra_menu.add_cascade(label="Cod.Lineal",menu=Linear)
        barra_menu.add_cascade(label="Ayuda",menu=ayudatr)

        s1 = Interfaz_Algebraica(root)
        s1.pantalla_algebraica()
        root.mainloop()

# x = principal_Algebraica()
# x.iniciar()