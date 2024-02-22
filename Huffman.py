from distutils.cmd import Command
from logging import root
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import fd
import numpy as np
import math 

import Hamming as hamm
import RLE as rle
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica
import pantalla_inicio as inicio
import Lineal as ln

class huffman():
    def __init__(self,probabili):
        self.probabilidad = probabili
        # [[0.30,'b'],[0.20,'c'],[0.15,'a'],[0.15,'e'],[0.10,'g'],[0.05,'d'],[0.05,'f']]
        pass
    
    def proceso(self):
       probabilidad = self.probabilidad
       #probabilidad = [[6/34,'E'],[4/34,'A'],[4/34,'C'],[3/34,'L'],[3/34,'S'],[2/34,'T'],[2/34,'O'],[2/34,'M'],[2/34,'U'],[2/34,'N'],[2/34,'I'],[1/34,'D'],[1/34,'G']]
       print(probabilidad)
       x = 0
       for i in range(len(probabilidad)):
            for j in range(len(probabilidad[i])):   
                if j == 0:
                    x += probabilidad[i][j]
       return probabilidad
    
    def hufman(self):
        prob = self.proceso()
        nueva = prob
        tam_original = len(prob)  
        recur = True
        while recur:
            tam = len(nueva)-1
            # print(nueva)
            momento = []
            suma_ultimo = nueva[tam-1][0]+nueva[tam][0]
            momento.append(suma_ultimo)
            for k in range(tam-1,tam+1):
                if nueva[0][0] < 1.0:
                    if k == tam-1:
                        for w in range(1,len(nueva[k])):
                            va = "0"+nueva[k][w]
                            momento.append(va)
                    elif k == tam:
                        for w in range(1,len(nueva[k])):
                            va = "1"+nueva[k][w]
                            momento.append(va)
            if tam > 1:    
                del nueva[tam]   
                del nueva[tam-1]
                con = 0
                conta = 0
                pos = 0
                posm = 0
                for i in range(len(nueva)):
                    if con == 0:
                        if suma_ultimo > nueva[i][0]:
                            # otra = otra.insert(i,momento) 
                            pos = i
                            posm = 1
                            con = 1
                        elif suma_ultimo == nueva[i][0]:
                            if conta == 0:
                                pos = i
                            posm = 0
                            conta += 1
                            # otra = otra.insert(i+1,momento)
                if posm == 0:        
                    nueva.insert(pos+conta,momento)
                elif posm == 1:
                    nueva.insert(pos,momento)
            elif tam == 1:
                # otra = otra.append(momento) 
                nueva.append(momento)
                del nueva[0:tam+1] 
            elif tam == 0:
                if nueva[0][0] == 1.0:
                    recur = False
        hufman = []
        nueva = nueva[0]
        fra = ""
        for i in range(len(nueva)):
            if i > 0:
                fra = nueva[i]
                frat = fra[len(fra)-1]
                fra = fra.replace(frat,"")
                fra = frat+" = "+fra 
                hufman.append(fra)
        return hufman


class Interfaz_huffman:
    def __init__(self,root):
        self.root = root
        self.frmhuffman = Frame()
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

    def calcuprobabilidad_automatica(self,frase):
        print(frase)
        frase_nueva =""
        ordenoriginal = []
        momento = []
        con = 0
        pos = 0
        conta = True
        condi = True
        for i in frase:
            if i != " ":
                frase_nueva += i 
        print(frase_nueva)
        tam = len(frase_nueva)
        if len(frase_nueva)<=40 and len(frase_nueva)>0 :
            for j in frase:
                for k in frase_nueva:
                    if j == k:
                        con += 1
                        if con == 1:
                            if len(ordenoriginal)>=1:
                                conta = True
                                for o in range(len(ordenoriginal)):
                                    for z in range(len(ordenoriginal[o])):
                                        if ordenoriginal[o][z] == k:
                                            conta = False
                                if conta:
                                    momento.append(k)                   
                            else:
                                momento.append(k)
                if j != " ":
                    condi = True
                    if len(ordenoriginal)>=1:
                        conta = True
                        for o in range(len(ordenoriginal)):
                            for z in range(len(ordenoriginal[o])):
                                if ordenoriginal[o][z] == j:
                                    conta = False
                        if conta:
                            momento.insert(0,con/tam)
                            for o in range(len(ordenoriginal)):
                                if condi:
                                    if momento[0] > ordenoriginal[o][0]:
                                        pos = o
                                        condi = False
                                    elif momento[0] == ordenoriginal[o][0]:
                                        pos += o+1
                                    else:
                                        pos = o+1   
                            ordenoriginal.insert(pos,momento)

                    else:
                        momento.insert(0,con/tam)
                        ordenoriginal.append(momento)
                    momento = []
                    con = 0
        else:
            messagebox.showwarning("Huffman","La frase es muy larga o no posee nada digite de nuevo :)")
            self.frase.set("")
        return ordenoriginal
        
    def conta_si(self,c,frase,redun):
        y = str(self.x.get())
        if redun == "1":
            if len(y)>0:
                if y != " ":
                    if self.conta >= 0:
                        if redun == "1":
                            c = self.conta
                            self.conta += 1
                            self.pantalla_si(frase,"0")
                            self.x.set("")
                    else:
                        self.conta += 1
            else:
                messagebox.showwarning("Huffman","Ingrese de nuevo el valor")
        return c

    def agrupar(self,tam):
        try:
            pos = 0
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

            v = self.unicos[self.conta][0]
            momento=[rta,v] 
            del self.unicos[self.conta]
            con = self.conta
            if self.conta>=1:
                condi = True
                for i in range(con):
                    if condi:
                        if momento[0] > self.unicos[i][0]:
                            pos = i
                            condi = False
                        elif momento[0] == self.unicos[i][0]:
                            pos = i+1
                        else:
                            pos = i+1   
            else: 
                pos = 0
            self.unicos.insert(pos,momento)
        except ValueError:
            messagebox.showwarning("Huffman","Ingrese de nuevo el valor")
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
            messagebox.showwarning("Huffman","La suma no da 1.0")
            self.pantalla_si(frase,"1")
        elif s == 1 or s == 0.99:
            orden = self.unicos
            self.pantalla_resultado(orden,frase)
        return confir
        
    def pantalla_si(self,frase,redun):
        
        self.frmsi.config(width="400",height="270",background="lavender",bd=10,relief="raised")
        frase_nueva = ""
        for i in frase:
            if i != " ":
                frase_nueva += i 

        vera = True
        
        if len(frase_nueva)<=40 and len(frase_nueva)>0 :
            self.frmhuffman.forget()
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
            messagebox.showwarning("Huffman","La frase es muy larga o no posee nada digite de nuevo :)")
            self.frase.set("")
        
        print(self.unicos)
        contador = self.conta_si(self.conta,frase,"0")
        print(contador)
        
        sobre = "longitud="+str(len(frase_nueva))

        lbltitulo = ttk.Label(self.frmsi,text="Ingrese las probabilidades en fracción",justify="center",font=(24),foreground="darkslategray",background="lavender")
        lbltitulo.grid(row=0,column=0,columnspan=3)

        # lblletra = ttk.Label(self.frmsi,text=self.unicos[contador],justify="center",font=(24),foreground="darkslategray",background="lavender")
        # lblletra.grid(row=1,column=0)

        frasetxt = Entry(self.frmsi,font=("consolas",10),textvariable=self.x,justify="center",background="lightsteelblue4",fg="lightcyan")
        frasetxt.grid(row=1,column=1)

        lblsobre = ttk.Label(self.frmsi,text=sobre,justify="center",font=(24),foreground="darkslategray",background="lavender")
        lblsobre.grid(row=1,column=2)

        

        if contador <= len(self.unicos)-1:
            lblletra = ttk.Label(self.frmsi,text=self.unicos[contador],justify="center",font=(24),foreground="darkslategray",background="lavender")
            lblletra.grid(row=1,column=0)

            btnsig = ttk.Button(self.frmsi,text="Añadir",style="MyButton.TButton"
                ,command=lambda:[self.agrupar(len(frase)),self.conta_si(contador,frase,"1")])
            btnsig.grid(row=2,column=0,columnspan=2)
        else:
            print(self.unicos)
            btnsig = ttk.Button(self.frmsi,text="Calcular",style="MyButton.TButton"
                ,command=lambda:[self.comprobar(frase)])
            btnsig.grid(row=2,column=0,columnspan=2)
        

    #pantalla de resultado
    def pantalla_resultado(self,ordenoriginal,frase):
        # print(frase)
        self.frmresultado = Frame()
        ordenamientooriginal = []
        ordenamientooriginal = ordenoriginal   
        print(ordenamientooriginal)
        h = huffman(ordenamientooriginal)  
        hufman1 = h.hufman()
        print(hufman1)
        self.frmhuffman.forget()
        self.frmsi.forget()
        self.frmresultado.pack()
        self.frmresultado.config(width="400",height="270",background="lavender",bd=10,relief="raised")
        
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="gray15",
        )
        lbltitu = ttk.Label(self.frmresultado,text="Resultado",justify="center",font=(24),foreground="darkslategray",background="lavender")
        lbltitu.grid(row=0,column=0,columnspan=3)
        conta = 0
        contasub = 1
        for i in range(len(hufman1)):
            a = hufman1[i]
            lbl = ttk.Label(self.frmresultado,text=a,foreground="darkslategray",background="lavender")
            lbl.grid(row=contasub,column=conta)
            conta += 1
            if conta == 3:
                contasub += 1
                conta = 0
        lblfrase =  ttk.Label(self.frmresultado,text=frase,justify="center",font=(24),foreground="darkslategray",background="lavender")
        lblfrase.grid(row=contasub+1,column=0,columnspan=3)
        final = ""
        for k in frase:
            if k != " ":
                for i in range(len(hufman1)):
                    x = hufman1[i]
                    tam = len(x)    
                    compa = x[0]
                    if k == compa:
                        final += x[4:tam+1]
            elif k == " ":
                    final += k
                    
        print(final)

        m = hamm.Hamming().hamming_fun(final)
        resultxt = Text(self.frmresultado,width=30, height=10,font=("consolas",12),background="lightsteelblue4")
        resultxt.insert('1.0',m)
        resultxt.grid(row=contasub+2,column=0,columnspan=3)

        btnregresar = ttk.Button(self.frmresultado,text="Regresar",style="MyButton.TButton"
            ,command=lambda:[self.frmresultado.destroy(),self.pantalla()])
        btnregresar.grid(row=contasub+3,column=1)

        



    #----------------------------------------------------------------funciones principales
    def probabilidad_automatica(self,frase):
        ordenoriginal = self.calcuprobabilidad_automatica(frase)
        # print(ordenoriginal)
        self.pantalla_resultado(ordenoriginal,frase)


    #-----------------------------------------------------------------------------pantalla
    def pantalla(self):
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="gray15",
        )
        s1 = ttk.Style()
        s1.configure(
            "MyButton.TButton",
            foreground="paleturquoise4",
            background="Seagreen1"
        )
        self.frmhuffman.pack()
        self.frmhuffman.config(width="400",height="270",background="lavender",bd=10,relief="raised")

        lbl = ttk.Label(self.frmhuffman,text="Ingrese la frase:",font=(48),foreground="darkslategray")
        lbl.config(background="lavender")
        lbl.place(x=110,y=10)

        frasetxt = Entry(self.frmhuffman,font=("consolas",10),textvariable=self.frase,justify="center",background="lightsteelblue4",fg="lightcyan")
        # frasetxt = Entry()
        frasetxt.place(x=40,y=50,width=300,height=50)

        lbl1 = ttk.Label(self.frmhuffman,text="Desea ingresar probabilidad",font=(48),foreground="darkslategray")
        lbl1.config(background="lavender")
        lbl1.place(x=60,y=120)

        btningresaprob = ttk.Button(self.frmhuffman,text="SI",style="MyButton.TButton"
            ,command=lambda:self.pantalla_si(frasetxt.get(),"1"))
        btningresaprob.place(x=60,y=160)

        btncalcularsinprob = ttk.Button(self.frmhuffman,text="NO",style="MyButton.TButton",
            command=lambda:self.probabilidad_automatica(frasetxt.get()))
        btncalcularsinprob.place(x=230,y=160)

        btncallimpiar = ttk.Button(self.frmhuffman,text="Limpiar",style="MyButtonL.TButton",
            command=lambda:self.limpiar())
        btncallimpiar.place(x=145,y=200)
        


class principal_huffman():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificacion Huffman")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_huffman.creador(self))


        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Aritmetica",command=lambda:[root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
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

        
        h1 = Interfaz_huffman(root)
        h1.pantalla()
        root.mainloop()


# h = principal_huffman()
# h.iniciar()