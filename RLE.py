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

import Hamming as hamm
import Huffman as hufman
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica
import pantalla_inicio as inicio
import Lineal as ln

class RLE():
    def __init__(self,matriz,num):
        self.mat = matriz
        self.n = num
        pass
    
    def zigzag(self):
        filas=self.n
        column=self.n

        #crea la cantidad de listas 
        mat_zigzag=[[] for i in range(filas+column-1)]
        mensaje = ""
        men_mat = []
        for i in range(filas):
            for j in range(column):
                sum=i+j
                if(sum%2 ==0):
        
                    #add at beginning
                    mat_zigzag[sum].insert(0,self.mat[i][j])
                else:
        
                    #add at end of the list
                    mat_zigzag[sum].append(self.mat[i][j])
        
        for k in range(len(mat_zigzag)):
            for p in range(len(mat_zigzag[k])):
                mensaje += str(mat_zigzag[k][p])
                men_mat.append(str(mat_zigzag[k][p]))
        return men_mat

    def horizontal(self):
        filas=self.n
        column=self.n
        mensaje = ""
        men_mat=[]
        for c in range(column):
            for f in range(filas):
                mensaje += str(self.mat[c][f])
                men_mat.append(str(self.mat[c][f]))
        return men_mat

    def vertical(self):
        filas=self.n
        column=self.n
        mensaje = ""
        men_mat=[]
        for c in range(column):
            for f in range(filas):
                mensaje += str(self.mat[f][c])
                men_mat.append(str(self.mat[f][c]))
        return men_mat
    
    def repeticiones(self,mensaje):
        p1 = ""
        total = len(mensaje)
        pos = 0
        mat_rle = []
        while pos < total:
            p1 = mensaje[pos]
            c = 0
            con = pos
            actu =con+1
            momen = []
            vera = True
            ver = True
            while vera:
                if ver:
                    if p1 == mensaje[con]:
                        c += 1 
                        n = p1
                        if con < total:
                            con += 1
                            actu += 1
                            if con == total:
                                ver = False
                    else:
                        vera = False
                        momen.append(c)
                        momen.append(n)
                else:
                    vera = False
                    momen.append(c)
                    momen.append(n)
                        
            mat_rle.append(momen)
            pos += c
        # print(mat_rle)
        return mat_rle

    def resultado_RLE(self,matr_rle):
        mat_orden = sorted(matr_rle)
        tam = len(matr_rle)
        nmayor = mat_orden[tam-1][0]
        binrio = bin(nmayor)
        t = len(binrio)
        binrio = binrio[2:t]
        tami = len(binrio)
        cod = ""
        for i in range(tam):
            codi = ""
            for j in range(len(matr_rle[i])):
                if j == 0:
                    n = matr_rle[i][j]
                    binrio = bin(n)
                    t = len(binrio)
                    binrio = binrio[2:t]
                    t = len(binrio)
                    if t < tami:
                      d = tami-t 
                      for p in range(d): 
                        binrio = "0"+binrio  
                    codi+=str(binrio)
                else:
                    codi=matr_rle[i][j]+codi
            cod += codi
        return cod

    def bit_bandera(self,mat_rle):
        mat_ordenrep = sorted(mat_rle,reverse=True)
        mat_rlerve = []
        for i in range(len(mat_rle)):
            momento = []
            momento.append(int(mat_rle[i][1]))
            momento.append(mat_rle[i][0])
            mat_rlerve.append(momento)
        
        mat_ordennum = sorted(mat_rlerve,reverse=TRUE)

        tam_matriz = len(mat_rle)

        nmayorrep = mat_ordenrep[0][0]
        nmayornum = mat_ordennum[0][0]

        binnmaoyrrep =bin(nmayorrep)
        binnmayornum = bin(nmayornum)

        ttemp = len(binnmaoyrrep)
        binnmaoyrrep =binnmaoyrrep[2:ttemp]
        ttemp = len(binnmayornum)
        binnmayornum = binnmayornum[2:ttemp]

        if nmayornum>=nmayorrep:
            tambits = len(binnmayornum)
        else:
            tambits = len(binnmaoyrrep)
        
        codificacion = ""

        for i in range(tam_matriz):
            codirep = ""
            codiinfo = ""
            for j in range(len(mat_rle[i])):
                if j == 0:
                    n = mat_rle[i][j]
                    binariorep = bin(n)
                    trep = len(binariorep)
                    binariorep = binariorep[2:trep]
                    trep = len(binariorep)
                    if trep < tambits:
                      d = tambits-trep 
                      for p in range(d): 
                        binariorep = "0"+binariorep
                    codirep="1"+str(binariorep)
                else:
                    n = mat_rle[i][j]
                    binarioinfo = bin(int(n))
                    tinfo = len(binarioinfo)
                    binarioinfo = binarioinfo[2:tinfo]
                    tinfo = len(binarioinfo)
                    if tinfo < tambits:
                      d = tambits-tinfo 
                      for p in range(d): 
                        binarioinfo = "0"+binarioinfo
                    codiinfo="0"+str(binarioinfo)
            codificacion += codirep+codiinfo
        return codificacion

        

    def byte_bandera(delf,mat_rle):
        mat_ordenrep = sorted(mat_rle,reverse=True)
        mat_rlerve = []
        for i in range(len(mat_rle)):
            momento = []
            momento.append(int(mat_rle[i][1]))
            momento.append(mat_rle[i][0])
            mat_rlerve.append(momento)
        
        mat_ordennum = sorted(mat_rlerve,reverse=TRUE)

        tam_matriz = len(mat_rle)

        nmayorrep = mat_ordenrep[0][0]
        nmayornum = mat_ordennum[0][0]

        binnmaoyrrep =bin(nmayorrep)
        binnmayornum = bin(nmayornum)

        ttemp = len(binnmaoyrrep)
        binnmaoyrrep =binnmaoyrrep[2:ttemp]
        ttemp = len(binnmayornum)
        binnmayornum = binnmayornum[2:ttemp]

        if nmayornum>=nmayorrep:
            tambits = len(binnmayornum)
        else:
            tambits = len(binnmaoyrrep)
        
        codificacion = ""

        for i in range(tam_matriz):
            codirep = ""
            codiinfo = ""
            unos = ""
            for j in range(len(mat_rle[i])):
                if j == 0:
                    n = mat_rle[i][j]
                    binariorep = bin(n)
                    trep = len(binariorep)
                    binariorep = binariorep[2:trep]
                    trep = len(binariorep)
                    if trep < tambits:
                      d = tambits-trep 
                      for p in range(d): 
                        binariorep = "0"+binariorep
                    for k in range(tambits):
                        unos += "1"
                    codirep=unos+str(binariorep)
                else:
                    n = mat_rle[i][j]
                    binarioinfo = bin(int(n))
                    tinfo = len(binarioinfo)
                    binarioinfo = binarioinfo[2:tinfo]
                    tinfo = len(binarioinfo)
                    if tinfo < tambits:
                      d = tambits-tinfo 
                      for p in range(d): 
                        binarioinfo = "0"+binarioinfo
                    codiinfo=str(binarioinfo)
            codificacion += codirep+codiinfo
        return codificacion
    
    def byte_anticipado(self,mat_rle):
        mat_ordenrep = sorted(mat_rle,reverse=True)
        mat_rlerve = []
        for i in range(len(mat_rle)):
            momento = []
            momento.append(int(mat_rle[i][1]))
            momento.append(mat_rle[i][0])
            mat_rlerve.append(momento)
        
        mat_ordennum = sorted(mat_rlerve,reverse=TRUE)

        tam_matriz = len(mat_rle)

        nmayorrep = mat_ordenrep[0][0]
        nmayornum = mat_ordennum[0][0]

        binnmaoyrrep =bin(nmayorrep)
        binnmayornum = bin(nmayornum)

        ttemp = len(binnmaoyrrep)
        binnmaoyrrep =binnmaoyrrep[2:ttemp]
        ttemp = len(binnmayornum)
        binnmayornum = binnmayornum[2:ttemp]

        if nmayornum>=nmayorrep:
            tambits = len(binnmayornum)
        else:
            tambits = len(binnmaoyrrep)
        
        codificacion = ""
        conanticipado = tambits
        limanticipado = tambits
        for i in range(tam_matriz):
            codirep = ""
            codiinfo = ""
            anticipado = ""
            for j in range(len(mat_rle[i])):
                if j == 0:
                    n = mat_rle[i][j]
                    binariorep = bin(n)
                    trep = len(binariorep)
                    binariorep = binariorep[2:trep]
                    trep = len(binariorep)
                    if trep < tambits:
                      d = tambits-trep 
                      for p in range(d): 
                        binariorep = "0"+binariorep
                    if conanticipado ==limanticipado:
                        if tambits %2 == 0:
                            
                            for k in range(limanticipado):
                                if k%2 == 0:    
                                    anticipado += "1"
                                else:
                                    anticipado += "0"
                            conanticipado = 0
                        else:
                            while conanticipado<=limanticipado:
                                if conanticipado%2 == 0:    
                                    anticipado += "1"
                                else:
                                    anticipado += "0"
                                conanticipado += 1
                            conanticipado = limanticipado
                            limanticipado += tambits
                    else:
                        anticipado = ""
                    codirep=anticipado+str(binariorep)
                    conanticipado+=1
                else:
                    n = mat_rle[i][j]
                    binarioinfo = bin(int(n))
                    tinfo = len(binarioinfo)
                    binarioinfo = binarioinfo[2:tinfo]
                    tinfo = len(binarioinfo)
                    if tinfo < tambits:
                      d = tambits-tinfo 
                      for p in range(d): 
                        binarioinfo = "0"+binarioinfo
                    codiinfo=str(binarioinfo)
                    conanticipado+=1
            codificacion += codirep+codiinfo
            
        return codificacion
    

                    

class Interfaz_RLE():
    def __init__(self,root):
        self.root = root
        self.frmRLE = Frame()
        self.frase = StringVar()
        self.de = StringVar()
        self.hasta = StringVar()
        self.valor = StringVar()
        self.seleccionTec = IntVar()
        self.seleccionLec = IntVar()
        self.mat = []
        self.lis = []
        pass
    
    def creador(self):
        messagebox.showinfo("Autores","Daniela Sosa Y Killiam Puentes")

    def limpiar(self):
        limpiar = " "
        self.frase.set(limpiar)
            
    def comparacion(self,num):
        rle_lecturas = RLE(self.mat,num)
        #mensajes
        menzigzag = rle_lecturas.zigzag()
        menhorizontal = rle_lecturas.horizontal()
        menverticl = rle_lecturas.vertical()
        #matrices de repeticion
        mat_zigzag = rle_lecturas.repeticiones(menzigzag)
        mat_horizontal = rle_lecturas.repeticiones(menhorizontal)
        mat_vertical = rle_lecturas.repeticiones(menverticl)
        #tamaño
        tzigzag = len(mat_zigzag)
        print(tzigzag)
        thorizontal = len(mat_horizontal)
        print(thorizontal)
        tvertical = len(mat_vertical)
        print(tvertical)
        if tzigzag<thorizontal and tzigzag<tvertical:
            messagebox.showwarning("RLE","Se recomienda lectura en Zigzag")
        elif thorizontal<tzigzag and thorizontal<tvertical:
            messagebox.showwarning("RLE","Se recomienda lectura en horizontal")
        elif tvertical<thorizontal and tvertical<tzigzag:
            messagebox.showwarning("RLE","Se recomienda lectura en vertical")
        elif tzigzag == thorizontal:
            messagebox.showwarning("RLE","Se recomienda lectura en horizontal y zigzag")
            if tzigzag == tvertical:
                messagebox.showwarning("RLE","Se recomienda cualquier lectura")
        elif tzigzag == tvertical:
            messagebox.showwarning("RLE","Se recomienda lectura en vertical y zigzag")
            if tzigzag == thorizontal:
                messagebox.showwarning("RLE","Se recomienda cualquier lectura")
        elif tvertical == thorizontal:
            messagebox.showwarning("RLE","Se recomienda lectura en vertical y horizontal")
            if tvertical == tzigzag:
                messagebox.showwarning("RLE","Se recomienda cualquier lectura")
    
    def esco(self,num):
        rle_lecturas = RLE(self.mat,num)
        codificacion = ""
        #mensajes
        menzigzag = rle_lecturas.zigzag()
        menhorizontal = rle_lecturas.horizontal()
        menverticl = rle_lecturas.vertical()
        #matrices de repeticion
        mat_zigzag = rle_lecturas.repeticiones(menzigzag)
        mat_horizontal = rle_lecturas.repeticiones(menhorizontal)
        mat_vertical = rle_lecturas.repeticiones(menverticl)
        if self.seleccionLec.get() == 1:
            mat_orde = mat_horizontal
            if self.seleccionTec.get()==1:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.bit_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menhorizontal,num,codificacion)
            elif self.seleccionTec.get()==2:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menverticl,num,codificacion)
            elif self.seleccionTec.get()==3:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_anticipado(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menzigzag,num,codificacion)
            else:
                messagebox.showwarning("RLE","Escoja una Tecnica de RLE")
        elif self.seleccionLec.get() == 2:
            mat_orde = mat_vertical
            if self.seleccionTec.get()==1:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.bit_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menhorizontal,num,codificacion)
            elif self.seleccionTec.get()==2:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menverticl,num,codificacion)
            elif self.seleccionTec.get()==3:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_anticipado(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menzigzag,num,codificacion)
            else:
                messagebox.showwarning("RLE","Escoja una Tecnica de RLE")
        elif self.seleccionLec.get() == 3:
            mat_orde = mat_zigzag
            if self.seleccionTec.get()==1:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.bit_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menhorizontal,num,codificacion)
            elif self.seleccionTec.get()==2:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_bandera(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menverticl,num,codificacion)
            elif self.seleccionTec.get()==3:
                self.frmrRLEinicio.destroy()
                codificacion = rle_lecturas.byte_anticipado(mat_orde)
                self.pantalla_resultadoRLE(mat_orde,menzigzag,num,codificacion)
            else:
                messagebox.showwarning("RLE","Escoja una Tecnica de RLE")
        else:
            messagebox.showwarning("RLE","Escoja una opcion de lectura")

        


    def mat_aleatoria(self,num):
        if num == "sofia":
            messagebox.showwarning("Power ranger aful","Te quiero canelo")
        try:
            num = int(num)
            if num>=2 and num<=20:
                aleatoria = []
                t = num*num
                contador = 0
                momen = []
                det = 0
                while contador < t:
                    if t < 4:
                        canti = random.randrange(1, 4, 1)
                    elif t<9:
                        canti = random.randrange(1, 7, 1)
                    elif t<100:
                        canti = random.randrange(1, 10, 1)
                    else:
                        canti = random.randrange(6, 15, 1)
                    contador += canti

                    while contador >t:
                        contador -= canti
                        canti = random.randrange(1, 11, 1)
                        contador += canti                
                
                    n = (random.randrange(1, 3, 1))-1
                    con = 1
                    while con <= canti:
                        if det == num:
                            det=0
                            aleatoria.append(momen)
                            momen=[]
                            momen.append(n)
                            det+=1
                        else:
                            momen.append(n)
                            det+=1
                        con+=1
                    if contador == t:
                        aleatoria.append(momen)
                    print(aleatoria)
                self.mat = np.array(aleatoria)
                self.pantalla_inicioRLE(num,"0")
            else:
                messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros de 2 a 20")
                self.frase.set("")
        except ValueError:
            messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros")
            self.frase.set("")

    def modificacion(self,de,hasta,valor,n):
        try:
            de = int(de)
            hasta = int(hasta)
            valor = int(valor)
            refe = []
            con = 1
            for f in range(n):
                momen = []
                for c in range(n):
                    momen.append(con)
                    con+=1
                refe.append(momen)
            refe = np.array(refe)

            #comparacion 
            ini = de
            vera = True
            i1 = refe[0][0]
            i2 = refe[n-1][n-1]
            if de >= i1 and de <=i2 and hasta >= i1 and hasta <= i2:
                for f in range(n):
                    for c in range(n):
                        nm = refe[f][c]
                        if vera:
                            if ini == nm:
                                self.mat[f][c] = valor
                                ini+=1
                                print(self.mat)
                                if ini == hasta+1:
                                    vera = False
                self.pantalla_manual(n,"1")
            else:
                messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros en el rango")
                self.de.set("")
                self.hasta.set("")
                self.pantalla_manual(n,"1")
        except ValueError:
            messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros")
            self.pantalla_manual(n,"1")
            self.de.set("")
            self.hasta.set("")
            self.valor.set("")
        

    def pantalla_manual(self,num,ver):
        self.frmmanu = Frame()
        if num == "sofia":
            messagebox.showwarning("Power ranger aful","Te quiero canelo")
        try:
            num = int(num)
            if num>=2 and num<=20:  
                con = 1
                mat_i = []
                if ver == "0":
                    for f in range(num):
                        momen = []
                        for c in range(num):
                            momen.append(con)
                            con+=1
                        mat_i.append(momen)
                    self.mat = np.array(mat_i)
                    self.lis = mat_i

                #pantalla manual
                self.frmRLE.forget()
                self.frmmanu.pack()
                self.frmmanu.config(width="400",height="260",background="mintcream",bd=10,relief="raised")
                posc = 0
                posf = 0

                lblre = ttk.Label(self.frmmanu,text="Matriz manual",font=(48),foreground="slateblue4",justify=CENTER)
                lblre.config(background="mintcream")
                lblre.grid(row=posf,column=posc,columnspan=num+2)

                for f in range(len(self.mat)):
                    posc = 1
                    posf += 1
                    for c in range(len(self.mat[f])):
                        p = str(self.mat[f][c])
                        print(p)
                        lbl = ttk.Label(self.frmmanu,text=p,foreground="steelblue",background="mintcream")
                        lbl.grid(row=posf,column=posc)
                        posc += 1
                
                posc = 0
                lblDe = ttk.Label(self.frmmanu,text="De",foreground="Deepskyblue4")
                lblDe.config(background="mintcream")
                lblDe.grid(row=posf+1,column=posc) 
                
                frasetxtde = Entry(self.frmmanu,font=("consolas"),textvariable=self.de,justify="center",background="cadetblue3",fg="slateblue4")
                frasetxtde.grid(row=posf+1,column=posc+1,columnspan=num) 

                posc = 0
                lblhasta = ttk.Label(self.frmmanu,text="Hasta",foreground="Deepskyblue4")
                lblhasta.config(background="mintcream")
                lblhasta.grid(row=posf+2,column=posc) 
                
                frasetxthasta = Entry(self.frmmanu,font=("consolas"),textvariable=self.hasta,justify="center",background="cadetblue3",fg="slateblue4")
                frasetxthasta.grid(row=posf+2,column=posc+1,columnspan=num)

                posc = 0
                lblvalor = ttk.Label(self.frmmanu,text="Numero",foreground="Deepskyblue4")
                lblvalor.config(background="mintcream")
                lblvalor.grid(row=posf+3,column=posc,columnspan=2) 
                
                frasetxtv = Entry(self.frmmanu,width=10,font=("consolas"),textvariable=self.valor,justify="center",background="cadetblue3",fg="slateblue4")
                frasetxtv.grid(row=posf+3,column=posc+1,columnspan=num)

                posc = 1
                btnmodifi = ttk.Button(self.frmmanu,text="modificar",style="MyButton.TButton",
                    command=lambda:[self.frmmanu.destroy(),self.modificacion(self.de.get(),self.hasta.get(),self.valor.get(),num)])
                btnmodifi.grid(row=posf+4,column=posc,columnspan=num)
                
                posc = 0
                btnPB = ttk.Button(self.frmmanu,text="Principal",style="MyButton.TButton",
                    command=lambda:[self.frmmanu.destroy(),self.pantalla_RLE()])
                btnPB.grid(row=posf+4,column=posc)

                posc = len(self.mat)+1    
                btnResul = ttk.Button(self.frmmanu,text="Resultado",style="MyButton.TButton",
                    command=lambda:[self.frmmanu.destroy(),self.pantalla_inicioRLE(num,"0")])
                btnResul.grid(row=posf+4,column=posc)
            else:
                messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros de 2 a 20")
                self.frase.set("")
        except ValueError:
            messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros")
            self.frase.set("")
        
    def pantalla_resultadoRLE(self,matriz,mensaje,num,codificacion):
        self.frmresultado = Frame()
        self.frmRLE.forget()
        self.frmresultado.pack()
        self.frmresultado.config(width="400",height="260",background="mintcream",bd=10,relief="raised")

        posc = 0
        posf = 0
        lblre = ttk.Label(self.frmresultado,text="Resultado",font=(48),foreground="slateblue4",justify=CENTER)
        lblre.config(background="mintcream")
        lblre.grid(row=posf,column=posc,columnspan=2)

        lblmen = ttk.Label(self.frmresultado,text="Mensaje",font=(12),foreground="slateblue4",justify=CENTER)
        lblmen.config(background="mintcream")
        lblmen.grid(row=posf+1,column=posc)

        mensajetxt = Text(self.frmresultado,width=45, height=7,font=("consolas",12),background="mintcream")
        mensajetxt.insert('1.0',mensaje)
        mensajetxt.grid(row=posf+1,column=posc+1)


        lblmatriz = ttk.Label(self.frmresultado,text="Matriz mensaje",font=(12),foreground="slateblue4",justify=CENTER)
        lblmatriz.config(background="mintcream")
        lblmatriz.grid(row=posf+2,column=posc)

        mattxt = Text(self.frmresultado,width=45, height=7,font=("consolas",12),background="mintcream")
        mattxt.insert('1.0',matriz)
        mattxt.grid(row=posf+2,column=posc+1)

        lblcodificacion = ttk.Label(self.frmresultado,text="Codificación",font=(12),foreground="slateblue4",justify=CENTER)
        lblcodificacion.config(background="mintcream")
        lblcodificacion.grid(row=posf+3,column=posc)

        m = hamm.Hamming().hamming_fun(codificacion)
        Codifitxt = Text(self.frmresultado,width=45, height=7,font=("consolas",12),background="mintcream")
        Codifitxt.insert('1.0',m)
        Codifitxt.grid(row=posf+3,column=posc+1)

        btnprincipal = ttk.Button(self.frmresultado,text="Principal",style="MyButton.TButton",
            command=lambda:[self.frmresultado.destroy(),self.pantalla_RLE()])
        btnprincipal.grid(row=posf+4,column=posc)

        btnvolver = ttk.Button(self.frmresultado,text="Volver",style="MyButton.TButton",
            command=lambda:[self.frmresultado.destroy(),self.pantalla_inicioRLE(num,"1")])
        btnvolver.grid(row=posf+4,column=posc+1)


    def pantalla_inicioRLE(self,num,v):
        try:
            num = int(num)
            self.frmrRLEinicio = Frame()
            self.frmRLE.forget()
            self.frmrRLEinicio.pack()
            self.frmrRLEinicio.config(width="400",height="260",background="mintcream",bd=10,relief="raised")

            posc = 0
            posf = 0
            lblre = ttk.Label(self.frmrRLEinicio,text="RLE Inicio",font=(48),foreground="slateblue4",justify=CENTER)
            lblre.config(background="mintcream")
            lblre.grid(row=posf,column=posc,columnspan=num+2)

            for f in range(len(self.mat)):
                    posc = 1
                    posf += 1
                    for c in range(len(self.mat[f])):
                        p = str(self.mat[f][c])
                        print(p)
                        lbl = ttk.Label(self.frmrRLEinicio,text=p,foreground="steelblue",background="mintcream")
                        lbl.grid(row=posf,column=posc)
                        posc += 1
            
            posc = num+1
            posfrb = 1
            lbllec = ttk.Label(self.frmrRLEinicio,text="Tecnica RLE",foreground="slateblue4",justify=CENTER)
            lbllec.config(background="mintcream")
            lbllec.grid(row=posfrb,column=posc)

            #radio buton izquierda
            posfrb += 1
            rbhorizontal = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Bit Bandera",variable=self.seleccionTec,value=1)
            rbhorizontal.grid(row=posfrb,column=posc)

            posfrb += 1
            rbvertical = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Byte Bandera",variable=self.seleccionTec,value=2)
            rbvertical.grid(row=posfrb,column=posc)

            posfrb += 1
            rbzigzag = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Byte anticipado",variable=self.seleccionTec,value=3)
            rbzigzag.grid(row=posfrb,column=posc)

            posc = 0
            posfrb = 1
            lbllec = ttk.Label(self.frmrRLEinicio,text="Lectura matriz",foreground="slateblue4",justify=CENTER)
            lbllec.config(background="mintcream")
            lbllec.grid(row=posfrb,column=posc)

            #radio buton derecha
            posfrb += 1
            posc = 0
            rbhorizontal = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Horizontal",variable=self.seleccionLec,value=1)
            rbhorizontal.grid(row=posfrb,column=posc)

            posfrb += 1
            rbvertical = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Vertical",variable=self.seleccionLec,value=2)
            rbvertical.grid(row=posfrb,column=posc)

            posfrb += 1
            rbzigzag = Radiobutton(self.frmrRLEinicio,background="mintcream",foreground="steelblue4",text="Zig-Zag",variable=self.seleccionLec,value=3)
            rbzigzag.grid(row=posfrb,column=posc)

            if posfrb >posf:
                posf = posfrb
            else:
                posf = posf
            posc = 0    
            btnprincipal = ttk.Button(self.frmrRLEinicio,text="Principal",style="MyButton.TButton",
                command=lambda:[self.frmrRLEinicio.destroy(),self.pantalla_RLE()])
            btnprincipal.grid(row=posf+1,column=posc)
            
            posc = 1    
            btncambiar = ttk.Button(self.frmrRLEinicio,text="Cambiar",style="MyButton.TButton"
                ,command=lambda:[self.pantalla_manual(num,"1"),self.frmrRLEinicio.destroy()])
            btncambiar.grid(row=posf+1,column=posc,columnspan=num)
            
            posc = num +1
            btncalcu = ttk.Button(self.frmrRLEinicio,text="Calcular",style="MyButton.TButton"
                ,command=lambda:[self.esco(num)])
            btncalcu.grid(row=posf+1,column=posc)

            if v == "0":
                self.comparacion(num)
            
        except ValueError:
            messagebox.showwarning("RLE","Ingrese de nuevo el valor solo se aceptan numeros")
            self.frase.set("")



#-----------------------------------------------------------------------------pantalla----------------------------------------------------------
    def pantalla_RLE(self):
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
        self.frmRLE.pack()
        self.frmRLE.config(width="400",height="260",background="mintcream",bd=10,relief="raised")

        lbl = ttk.Label(self.frmRLE,text="Ingrese la el tamaño de la matriz:2-20",font=(48),foreground="steelblue")
        lbl.config(background="mintcream")
        lbl.place(x=30,y=10)

        frasetxt = Entry(self.frmRLE,font=("consolas",14),textvariable=self.frase,justify="center",background="cadetblue3",fg="slateblue4")
        # frasetxt = Entry()
        frasetxt.place(x=40,y=50,width=300,height=50)

        lbl1 = ttk.Label(self.frmRLE,text="Modificar matriz de forma:",font=(48),foreground="steelblue")
        lbl1.config(background="mintcream")
        lbl1.place(x=60,y=120)

        btnmanual = ttk.Button(self.frmRLE,text="Manual",style="MyButton.TButton"
            ,command=lambda:self.pantalla_manual(self.frase.get(),"0"))
        btnmanual.place(x=60,y=160)

        btncalautoma = ttk.Button(self.frmRLE,text="automatica",style="MyButton.TButton"
            ,command=lambda:self.mat_aleatoria(self.frase.get()))
        btncalautoma.place(x=230,y=160)
      
        btncallimpiar = ttk.Button(self.frmRLE,text="Limpiar",style="MyButtonL.TButton",
            command=lambda:self.limpiar())
        btncallimpiar.place(x=150,y=200)      

class principal_RLE():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificacion RLE")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_RLE.creador(self))
        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="Huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Aritmetica",command=lambda:[root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
        Canal.add_command(label="Algebraica",command=lambda:[root.destroy(),algebraica.principal_Algebraica.iniciar(self)])
                
    

        Linear = Menu(barra_menu,tearoff=0)
        Linear.add_command(label="Lineal",command=lambda:[root.destroy(),ln.principal_Lineal.iniciar(self)])

        barra_menu.add_cascade(label="inicio",menu=Inicio)
        barra_menu.add_cascade(label="Cod.Canal",menu=Canal)
        barra_menu.add_cascade(label="Cod.Lineal",menu=Linear)
        barra_menu.add_cascade(label="Ayuda",menu=ayudatr)

        s1 = Interfaz_RLE(root)
        s1.pantalla_RLE()
        root.mainloop()

# x = principal_RLE()
# x.iniciar()