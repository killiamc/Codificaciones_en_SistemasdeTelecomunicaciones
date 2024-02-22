from distutils.cmd import Command
from logging import root
from operator import le
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import color, fd
import math 
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import Hamming as hamm
import Huffman as hufman
import Shanonfanon_Final as shannon
import Cod_algbraica as algebraica
import pantalla_inicio as inicio
import Lineal as ln
import RLE as rle

class Cod_Aritmetica():
    def __init__(self,matriz,fr):
        self.mat_arit = matriz
        self.frase = fr
    
    def Aritmerica(self):
        frase = self.frase
        momento = [0,1]
        for i in frase:
            for p in range(len(self.mat_arit)):
                if self.mat_arit[p][2] == i:
                    aactu = momento[0]
                    bactu = momento[1]
                    ai = self.mat_arit[p][0]
                    bi = self.mat_arit[p][1]
                    p1 = aactu+(bactu-aactu)*ai
                    p2 = aactu+(bactu-aactu)*bi
                    momento = [p1,p2]
        return momento

    def redondeo(self):
        completo = self.Aritmerica()
        valor = round(completo[0],len(self.frase)+5)
        tam = len(str(valor))-2
        acabo = True
        v = valor
        con = -1
        num = 0
        bits = []
        f_bits = ""
        while acabo:
            nuevo_v = v*2
            if nuevo_v >= 1:
                en = nuevo_v // 1
                b = "1"
            else:
                en = 0
                b="0"
            f_bits += b
            bits.append(b)
            v = nuevo_v-en
            vali = 2**con
            num += vali*en
            x = round(num,tam)
            con-=1
            if x == valor:
                acabo = False
        return valor,f_bits
    

    

class Interfaz_Aritmetica():
    def __init__(self,root):
        self.root = root
        self.frmAritmetica = Frame()
        self.frmsi = Frame()
        self.frase = StringVar()
        self.x = StringVar()
        self.conta = 0
        self.unicos = []
        pass
    
    def creador(self):
        messagebox.showinfo("Autores","Daniela Sosa Y Killiam Puentes")

    def limpiar(self):
        limpiar = " "
        self.frase.set(limpiar)

    def conta_si(self,c,frase,redun):
        y = str(self.x.get())
        if redun == "1":
            if len(y)>0:
                if y != " ":
                    if self.conta >= 0:
                        if redun == "1":
                            c = self.conta
                            self.conta += 1
                            self.pantalla_calculo(frase,"0")
                            self.x.set("")
                    else:
                        self.conta += 1
            else:
                messagebox.showwarning("Codificación Aritmetica","Ingrese de nuevo el valor")
        return c

    def agrupar(self,tam):
        try:
            y = str(self.x.get())
            momento = []
            recur = 1
            i = 0
            t = len(y)
            for j in y:
                if j == "/":
                    num = float(y[0:i])
                    den = float(y[i+1:t])  
                    recur = 0
                i += 1
            if recur == 1:
                rta = float(y)
            elif recur == 0:
                rta = num/den 
            rta = round(rta,t)
            if rta >= 1:
                messagebox.showwarning("Codificación Aritmetica","EL valor no puede ser mayor a 1")
                self.x.set(" ")
            else:
                v = self.unicos[self.conta][0]
                momento=[rta,v] 
                del self.unicos[self.conta]
                con = self.conta
                self.unicos.insert(con,momento)
        except ValueError:
            messagebox.showwarning("Codificación Aritmetica","Ingrese de nuevo el valor")
            self.x.set(" ")

    def comprobar(self,frase):
        s = 0
        for i in range(len(self.unicos)):
            s += self.unicos[i][0]
        confir = ""
        s = round(s,2)
        print(s)
        if s > 1 or s<0.99:
            del self.unicos[0:self.conta]
            print(self.unicos)
            self.conta= 0
            self.unicos = []
            messagebox.showwarning("Codificación Aritmetica","La suma no da 1.0")
            self.pantalla_calculo(frase,"1")
        elif s == 1 or s == 0.99:
            matriz_arit=[]
            momento = []
            for i in range(len(self.unicos)):
                if i >= 1:
                    a = matriz_arit[i-1][1]
                    ta = len(str(a))
                    b_1 = self.unicos[i][0]
                    tb1 = len(str(b_1))
                    if a>b_1:
                        b = round(a+b_1,ta-1)
                    else:
                        b = round(a+b_1,tb1-1)
                    va = self.unicos[i][1]
                    momento = [a,b,va]
                else:
                    a = 0
                    b = self.unicos[i][0]
                    va = self.unicos[i][1]
                    momento = [a,b,va]
                matriz_arit.append(momento)
            self.unicos.clear
            self.unicos=matriz_arit
            self.pantalla_resultado(frase)
        return confir

    def pantalla_calculo(self,frase,redun):
        
        self.frmsi.config(width="400",height="270",background="cornsilk3",bd=10,relief="raised")
        frase_nueva = frase
        
        if len(frase_nueva)<=20 and len(frase_nueva)>0 :
            self.frmAritmetica.forget()
            self.frmsi.pack()
            if redun == "1":
                self.conta=0
                self.unicos = []
                for i in frase_nueva:
                        vera = True
                        momento = []
                        for j in frase:
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
        else:
            messagebox.showwarning("Codificación Aritmetica","La frase es muy larga o no posee nada digite de nuevo :)")
            self.frase.set("")
        
        print(self.unicos)
        contador = self.conta_si(self.conta,frase,"0")
        print(contador)
        
        sobre = "longitud="+str(len(frase_nueva))
        titulo = "Ingrese las probabilidades en fracción"

        lbltitulo = ttk.Label(self.frmsi,text=titulo,justify="center",font=(24),foreground="Darkorange4",background="cornsilk3")
        lbltitulo.grid(row=0,column=0,columnspan=3)

        frasetxt = Entry(self.frmsi,font=("consolas",10),textvariable=self.x,justify="center",background="lightsteelblue4",fg="lightcyan")
        frasetxt.grid(row=1,column=1)

        lblsobre = ttk.Label(self.frmsi,text=sobre,justify="center",font=(24),foreground="DarkOrange4",background="cornsilk3")
        lblsobre.grid(row=1,column=2)

        
        if contador <= len(self.unicos)-1:
            lblletra = ttk.Label(self.frmsi,text=self.unicos[contador],justify="center",font=(24),foreground="DarkOrange4",background="cornsilk3")
            lblletra.grid(row=1,column=0) 

            btnsig = ttk.Button(self.frmsi,text="Añadir",style="MyButton.TButton"
                ,command=lambda:[self.agrupar(len(frase)),self.conta_si(contador,frase,"1")])
            btnsig.grid(row=2,column=0,columnspan=2)

        else:

            print(self.unicos)
            btnsig = ttk.Button(self.frmsi,text="Calcular",style="MyButton.TButton"
                ,command=lambda:[self.comprobar(frase)])
            btnsig.grid(row=2,column=0,columnspan=2)

    def pantalla_deco(self,num,matriz):
        self.frmdeco = Frame()
        self.frmdeco.config(width="400",height="270",background="cornsilk3",bd=10,relief="raised")
        self.frmdeco.pack()
        lbltitu = ttk.Label(self.frmdeco,text="Decodificación",justify="center",font=(24),foreground="DarkOrange4",background="cornsilk3")
        lbltitu.grid(row=0,column=0,columnspan=3)

        momen = num
        c = 0
        vali = True
        frase_deco = ""
        contapos = 1


        while vali:
            for i in range(len(matriz)):
                if momen >= matriz[i][0]:
                    if momen < matriz[i][1]:
                        
                        if contapos == 1:
                            lbl = ttk.Label(self.frmdeco,text="inicio",foreground="DarkOrange4",background="cornsilk3")
                            lbl.grid(row=contapos,column=0)  

                            lbl1 = ttk.Label(self.frmdeco,text=str(momen),foreground="DarkOrange4",background="cornsilk3")
                            lbl1.grid(row=contapos,column=1)

                        elif contapos >1:
                            frase_deco += matriz[i][2]
                            m = str(momen)
                            aac = str(matriz[i][0])
                            bac =str(matriz[i][1])
                            fr = "(" +m+"-"+aac+")/("+bac+"-"+aac+")"+" = "

                            lbl = ttk.Label(self.frmdeco,text=fr,foreground="DarkOrange4",background="cornsilk3")
                            lbl.grid(row=contapos,column=0)

                            momen = round((momen-matriz[i][0])/(matriz[i][1]-matriz[i][0]),len(str(num))-1)

                            lbl1 = ttk.Label(self.frmdeco,text=str(momen),foreground="DarkOrange4",background="cornsilk3")
                            lbl1.grid(row=contapos,column=1)

                            lblr =ttk.Label(self.frmdeco,text=matriz[i][2],foreground="DarkOrange4",background="cornsilk3")
                            lblr.grid(row=contapos-1,column=2) 
                        contapos+=1
                        if momen == 0:
                            vali = False
                            lblr =ttk.Label(self.frmdeco,text="final",foreground="DarkOrange4",background="cornsilk3")
                            lblr.grid(row=contapos-1,column=2) 
    
        frdeco = "Frase = "+ frase_deco
        lblfr =ttk.Label(self.frmdeco,text=frdeco,foreground="Orangered4",font=24,background="cornsilk3")
        lblfr.grid(row=contapos,column=0,columnspan=3) 
        
        btnregresar = ttk.Button(self.frmdeco,text="Inicio",style="MyButton.TButton"
            ,command=lambda:[self.frmdeco.destroy(),self.pantalla()])
        btnregresar.grid(row=contapos+1,column=0,columnspan=2)

        btnDecodificar = ttk.Button(self.frmdeco,text="Codificar",style="MyButton.TButton"
            ,command=lambda:[self.frmdeco.destroy(),self.pantalla_resultado(frase_deco)])
        btnDecodificar.grid(row=contapos+1,column=2,columnspan=2)
        

    def pantalla_resultado(self,frase):
        self.frmresultado = Frame()
        matriz_a = self.unicos
        print(self.unicos)
        p = Cod_Aritmetica(matriz_a,frase)
        valor,bits=p.redondeo()
        self.frmAritmetica.forget()
        self.frmsi.forget()
        self.frmresultado.pack()
        self.frmresultado.config(width="400",height="270",background="cornsilk3",bd=10,relief="raised")
        
        # paso = 10
        # t = np.linspace(0,1,paso)
        # con  =1
        # fig = Figure(figsize=(2,2),dpi=200)
        # fig2, ax = plt.subplots(figsize=(1,1),dpi=100)     
        '''
        for i in range(len(matriz_a)):
            p = round(paso/len(matriz_a))
            t_1 = np.linspace(matriz_a[i][0],matriz_a[i][1],int(10))
            y1= np.ones(len(t_1))
            if con == 1:
                esti = "--"
                co = "c"
                fig2.add_subplot(va).plot(t_1,y1,esti,color=co)
                if i == 1:
                    ax.axes.get_yaxis().set_visible(True)
                else:
                    ax.axes.get_yaxis().set_visible(False)
            elif con ==2:
                esti= "None"
                co = "darkgreen"
                fig2.add_subplot(va).plot(t_1,y1,esti,color=co)
                ax.axes.get_yaxis().set_visible(False)
            elif con ==3:
                esti = "."
                co = "red"
                fig2.add_subplot(va).plot(t_1,y1,esti,color=co)
                ax.axes.get_yaxis().set_visible(False)
            elif con == 4:
                esti = "o"
                co = "skyblue"
                fig2.add_subplot(va).plot(t_1,y1,esti,color=co)
                ax.axes.get_yaxis().set_visible(False)
            elif con ==5:
                esti = "+"
                co = "k"
                fig2.add_subplot(va).plot(t_1,y1,esti,color=co)
                ax.axes.get_yaxis().set_visible(False)

            con += 1
            canvas = FigureCanvasTkAgg(fig2,master=self.frmresultado)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1,column=0)
            
            va += 1
            if con > 5:
                con = 1      
        '''
        lbltitu = ttk.Label(self.frmresultado,text="Resultado",justify="center",font=(24),foreground="DarkOrange4",background="cornsilk3")
        lbltitu.grid(row=0,column=0,columnspan=2)

        max = 300
        w = Canvas(self.frmresultado, width=max, height=40)
        w.grid(row=1,column=0)
        con = 1
        for i in range(len(matriz_a)):
            if con == 1:
                co = "cyan"
            elif con ==2:
                co = "darkgreen"
            elif con ==3:
                co = "turquoise"
            elif con == 4:
                co = "skyblue"
            elif con ==5:
                co = "medium spring green"
            ini = matriz_a[i][0]*max
            final = matriz_a[i][1]*max
            w.create_rectangle(ini, 0, final, 25, fill=co)
            lim = str(round(matriz_a[i][1],2))
            centro = round(((final-ini)/2))+ini
            if i <len(matriz_a)-1:
                vaf = lim[1:len(lim)]
                print(i)
            else:
                vaf = lim
            w.create_text(centro, 13, text=matriz_a[i][2], fill='black')
            w.create_text(final, 34, text=vaf, fill='DarkOrange4')
            con+=1
            if con > 5:
                con = 1      

        txt = "valor ="
        txt =txt+str(valor)
        lblvalor = ttk.Label(self.frmresultado,text=txt,justify="center",font=(24),foreground="DarkOrange4",background="cornsilk3")
        lblvalor.grid(row=2,column=0)

        m = hamm.Hamming().hamming_fun(bits)
        resultxt = Text(self.frmresultado,width=30, height=10,font=("consolas",12),background="wheat1")
        resultxt.insert('1.0',m)
        resultxt.grid(row=3,column=0,columnspan=2)

        btnregresar = ttk.Button(self.frmresultado,text="Inicio",style="MyButton.TButton"
            ,command=lambda:[self.frmresultado.destroy(),self.pantalla()])
        btnregresar.grid(row=4,column=0,columnspan=2)

        btnDecodificar = ttk.Button(self.frmresultado,text="Decodificar",style="MyButton.TButton"
            ,command=lambda:[self.frmresultado.destroy(),self.pantalla_deco(valor,matriz_a)])
        btnDecodificar.grid(row=4,column=1,columnspan=2)

    def pantalla(self):
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="DarkOrange4",
        )

        s1 = ttk.Style()
        s1.configure(
            "MyButton.TButton",
            foreground="DarkOrange4",
            background="orange"
        )
        self.frmAritmetica.pack()
        self.frmAritmetica.config(width="400",height="230",background="cornsilk3",bd=10,relief="raised")

        lbl = ttk.Label(self.frmAritmetica,text="Ingrese la frase:",font=(52),foreground="DarkOrange4")
        lbl.config(background="cornsilk3")
        lbl.place(x=120,y=10)

        frasetxt = Entry(self.frmAritmetica,font=("consolas",10),textvariable=self.frase,justify="center",background="lightsteelblue4",fg="lightcyan")
        frasetxt.place(x=40,y=50,width=300,height=60)

        btningresaprob = ttk.Button(self.frmAritmetica,text="Calcular",style="MyButton.TButton"
            ,command=lambda:self.pantalla_calculo(frasetxt.get(),"1"))
        btningresaprob.place(x=100,y=150)

        btncallimpiar = ttk.Button(self.frmAritmetica,text="Limpiar",style="MyButtonL.TButton",
            command=lambda:self.limpiar())
        btncallimpiar.place(x=200,y=150)


class principal_Aritmetica():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificacion Aritmetica")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_Aritmetica.creador(self))

        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="Huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Algebraica",command=lambda:[root.destroy(),algebraica.principal_Algebraica.iniciar(self)])
                
        rLe = Menu(barra_menu,tearoff=0)
        rLe.add_command(label="RLE",command=lambda:[root.destroy(),rle.principal_RLE.iniciar(self)])

        Linear = Menu(barra_menu,tearoff=0)
        Linear.add_command(label="Lineal",command=lambda:[root.destroy(),ln.principal_Lineal.iniciar(self)])

        barra_menu.add_cascade(label="inicio",menu=Inicio)
        barra_menu.add_cascade(label="Cod.Canal",menu=Canal)
        barra_menu.add_cascade(label="RLE",menu=rLe)
        barra_menu.add_cascade(label="Cod.Lineal",menu=Linear)
        barra_menu.add_cascade(label="Ayuda",menu=ayudatr)
        s1 = Interfaz_Aritmetica(root)
        s1.pantalla()
        root.mainloop()

ps =principal_Aritmetica()
ps.iniciar()