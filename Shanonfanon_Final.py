from distutils.cmd import Command
from logging import root
from pickle import FRAME
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import fd
import math 

import Hamming as hamm
import Huffman as hufman
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica
import pantalla_inicio as inicio
import Lineal as ln
import RLE as rle

class shanon_fanon():
    def __init__(self,probabili):
        self.probabilidad = probabili

    def comprobacion(self,vector):
        con_presen = 0
        con_futuro = 0
        vera = True
        pos = 0
        sum = 0
        for i in range(len(vector)):
            sum += vector[i][0]    
        PmI = sum/2
        #dividir el vector
        for i in range(len(vector)):
            if vera:
                con_presen += vector[i][0]
                con_futuro = con_presen +vector[i+1][0]
                if con_futuro >= PmI:     
                   if con_futuro == PmI:
                        mi_1 = vector[0:i+2]
                        mi_2 = vector[i+2:len(vector)]
                        pos = i+2
                        vera = False
                   else:            
                        RcF = con_futuro-PmI
                        RcP = PmI-con_presen
                        if RcF > RcP:
                            mi_1 = vector[0:i+1]
                            mi_2 = vector[i+1:len(vector)]
                            vera = False
                            pos = i+1
                        elif RcP >RcF:
                            mi_1 = vector[0:i+2]
                            mi_2 = vector[i+2:len(vector)]
                            vera = False
                            pos = i+2
                        elif RcF == RcP:
                            mi_1 = vector[0:i+1]
                            mi_2 = vector[i+1:len(vector)]
                            vera = False
                            pos = i+1
        return mi_1,mi_2,pos

    def asignacion(self,pos,matrizF,lim,inicio):
        for i in range(inicio,lim):
            if i < pos:
                m = "0"
                matrizF[i].append(m)
            else:
                m = "1"
                matrizF[i].append(m)
            i += 1
        return matrizF


    def evaluacion_mitad(self,mit_0,mit_1,mat_final,ini,p1,pos):
        j = 0
        conta = 1
        while j < conta:
            if len(mit_0)>2:
                a_0,a_1,pos = self.comprobacion(mit_0)
                conta += 1
            else:
                if len(mit_0)==2:
                    mat_final = self.asignacion(p1-1,mat_final,p1,ini)
            if len(mit_1)>2:
                a_0,a_1,p = self.comprobacion(mit_1)
                ini = p1
                p1 += p 
                mat_final = self.asignacion(p1,mat_final,pos,ini)      
                conta += 1
                mit_0 = a_0
                mit_1 = a_1
            else:
                if len(mit_1)==2:
                    mat_final = self.asignacion(pos-1,mat_final,pos,p1)
            j += 1   
        return mat_final
    
    def shanon_f(self):
        probabilidad = self.probabilidad
        mi_0,mi_1,pos = self.comprobacion(probabilidad)
        final = self.asignacion(pos,probabilidad,len(probabilidad),0)
        conta = 1
        j = 0
        ini = 0
        p = 0
        p1 = 0
        while j < conta:
            if len(mi_0)>2:
                a_0,a_1,p1 = self.comprobacion(mi_0)
                p1 = ini + p1
                final = self.asignacion(p1,final,pos,ini)  
                final = self.evaluacion_mitad(a_0,a_1,final,ini,p1,pos)
                j += 1
                conta += 1
            else:
                if len(mi_0)==2:
                    final = self.asignacion(pos-1,final,pos,ini)
            if len(mi_1)>2:
                a_0,a_1,p = self.comprobacion(mi_1)
                ini = pos
                pos += p 
                final = self.asignacion(pos,final,len(final),ini)             
                conta += 1
                mi_0 = a_0
                mi_1 = a_1
            else:
                if len(mi_1)==2:
                    final = self.asignacion(len(final)-1,final,len(final),pos)
            j += 1  
        return final
    
    def entropia(self):
        fl = self.probabilidad
        ShanonF_entropia = []
        for i in range(len(fl)):
            f = ""
            momento = []
            a = fl[i][0]
            momento.append(a)
            a = fl[i][1]
            momento.append(a)
            lim_mom = len(fl[i])
            p = fl[i][2:lim_mom]
            s = "".join(p)
            f = f+s
            momento.append(f)
            ShanonF_entropia.append(momento)
        print(ShanonF_entropia)
        #longitud promedio
        lpr = 0
        h = 0
        for j in range(len(ShanonF_entropia)):
            pi = ShanonF_entropia[j][0]
            caracter = ShanonF_entropia[j][2]
            li = len(caracter)
            lpr += pi*li #logitud pormedio
            h += -pi*math.log(pi,2)#entropia
        n = h/lpr #eficiencia
        m = len(ShanonF_entropia)
        r = (math.log(m,2))/lpr #tasa de compresion 
        return lpr,h,n,r

    def rtashanon(self):
        final = self.shanon_f()
        ShanonF_final = []
        for i in range(len(final)):
            f = ""
            lim_mom = len(final[i])
            f = final[i][1]
            f = f + " = "
            p = final[i][2:lim_mom]
            s = "".join(p)
            f = f+s
            ShanonF_final.append(f)
        return ShanonF_final




class Interfaz_ShanonF:
    def __init__(self,root):
        self.root = root
        self.frmShanonFanon = Frame()
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
            messagebox.showwarning("Shanon Fanon","La frase es muy larga o no posee nada digite de nuevo :)")
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
                messagebox.showwarning("Shanon Fanon","Ingrese de nuevo el valor")
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
            messagebox.showwarning("Shanon Fanon","Ingrese de nuevo el valor")
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
            messagebox.showwarning("Shanon Fanon","La suma no da 1.0")
            self.pantalla_si(frase,"1")
        elif s == 1 or s == 0.99:
            orden = self.unicos
            self.pantalla_resultado(orden,frase)
        return confir
        
    def pantalla_si(self,frase,redun):
        if frase == "karen":
            messagebox.showwarning("Power ranger aful","Te quiero canelo")
        self.frmsi.config(width="400",height="270",background="Tan1",bd=10,relief="raised")
        frase_nueva = ""
        for i in frase:
            if i != " ":
                frase_nueva += i 

        vera = True
        
        if len(frase_nueva)<=40 and len(frase_nueva)>0 :
            self.frmShanonFanon.forget()
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
            messagebox.showwarning("Shanon Fanon","La frase es muy larga o no posee nada digite de nuevo :)")
            self.frase.set("")
        
        print(self.unicos)
        contador = self.conta_si(self.conta,frase,"0")
        print(contador)
        
        sobre = "longitud="+str(len(frase_nueva))

        lbltitulo = ttk.Label(self.frmsi,text="Ingrese las probabilidades en fracción",justify="center",font=(24),foreground="green4",background="Tan1")
        lbltitulo.grid(row=0,column=0,columnspan=3)

        # lblletra = ttk.Label(self.frmsi,text=self.unicos[contador],justify="center",font=(24),foreground="darkslategray",background="lavender")
        # lblletra.grid(row=1,column=0)

        frasetxt = Entry(self.frmsi,font=("consolas",10),textvariable=self.x,justify="center",background="lightsteelblue4",fg="lightcyan")
        frasetxt.grid(row=1,column=1)

        lblsobre = ttk.Label(self.frmsi,text=sobre,justify="center",font=(24),foreground="green4",background="Tan1")
        lblsobre.grid(row=1,column=2)

        

        if contador <= len(self.unicos)-1:
            lblletra = ttk.Label(self.frmsi,text=self.unicos[contador],justify="center",font=(24),foreground="green4",background="Tan1")
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
        sF = shanon_fanon(ordenamientooriginal)
        ShanonF = sF.rtashanon()
        lpr,h,n,r = sF.entropia()
        print(ShanonF)
        self.frmShanonFanon.forget()
        self.frmsi.forget()
        self.frmresultado.pack()
        self.frmresultado.config(width="400",height="270",background="Tan1",bd=10,relief="raised")
        
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="gray15",
        )
        lbltitu = ttk.Label(self.frmresultado,text="Resultado",justify="center",font=(24),foreground="green4",background="Tan1")
        lbltitu.grid(row=0,column=0,columnspan=3)
        conta = 0
        contasub = 1
        for i in range(len(ShanonF)):
            a = ShanonF[i]
            lbl = ttk.Label(self.frmresultado,text=a,foreground="green4",background="Tan1")
            lbl.grid(row=contasub,column=conta)
            conta += 1
            if conta == 3:
                contasub += 1
                conta = 0
        lblfrase =  ttk.Label(self.frmresultado,text=frase,justify="center",font=(24),foreground="green4",background="Tan1")
        lblfrase.grid(row=contasub+1,column=0,columnspan=3)
        final = ""
        for k in frase:
            if k != " ":
                for i in range(len(ShanonF)):
                    x = ShanonF[i]
                    tam = len(x)    
                    compa = x[0]
                    if k == compa:
                        final += x[4:tam+1]
            # elif k == " ":
            #         final += k
                    
        print(final)
        m = hamm.Hamming().hamming_fun(final)
        resultxt = Text(self.frmresultado,width=30, height=10,font=("consolas",12),background="darkslategray")
        resultxt.insert('1.0',m)
        resultxt.grid(row=contasub+2,column=0,columnspan=3)
        #entropia

        p = "longitud = "+str(round(lpr,2))
        lbl_lpr = ttk.Label(self.frmresultado,text=p,foreground="green4",background="Tan1")
        lbl_lpr.grid(row=contasub+3,column=0)

        p = "Entropia = "+str(round(h,2))
        lbl_h = ttk.Label(self.frmresultado,text=p,foreground="green4",background="Tan1")
        lbl_h.grid(row=contasub+4,column=0)

        p = "Eficiencia = "+str(round(n,2))
        lbl_n = ttk.Label(self.frmresultado,text=p,foreground="green4",background="Tan1")
        lbl_n.grid(row=contasub+3,column=1)

        p = "compresion = "+str(round(r,2))
        lbl_r = ttk.Label(self.frmresultado,text=p,foreground="green4",background="Tan1")
        lbl_r.grid(row=contasub+4,column=1)

        btnregresar = ttk.Button(self.frmresultado,text="Regresar",style="MyButton.TButton"
            ,command=lambda:[self.frmresultado.destroy(),self.pantalla()])
        btnregresar.grid(row=contasub+3,column=2,rowspan=2)


    #----------------------------------------------------------------funciones principales
    def probabilidad_automatica(self,frase):
        ordenoriginal = self.calcuprobabilidad_automatica(frase)
        if frase == "karen":
            messagebox.showwarning("Power ranger aful","Te quiero canelo")
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
        self.frmShanonFanon.pack()
        self.frmShanonFanon.config(width="400",height="270",background="Tan1",bd=10,relief="raised")

        lbl = ttk.Label(self.frmShanonFanon,text="Ingrese la frase:",font=(48),foreground="green4")
        lbl.config(background="Tan1")
        lbl.place(x=110,y=10)

        frasetxt = Entry(self.frmShanonFanon,font=("consolas",10),textvariable=self.frase,justify="center",background="lightsteelblue4",fg="lightcyan")
        # frasetxt = Entry()
        frasetxt.place(x=40,y=50,width=300,height=50)

        lbl1 = ttk.Label(self.frmShanonFanon,text="Desea ingresar probabilidad",font=(48),foreground="green4")
        lbl1.config(background="Tan1")
        lbl1.place(x=60,y=120)

        btningresaprob = ttk.Button(self.frmShanonFanon,text="SI",style="MyButton.TButton"
            ,command=lambda:self.pantalla_si(frasetxt.get(),"1"))
        btningresaprob.place(x=60,y=160)

        btncalcularsinprob = ttk.Button(self.frmShanonFanon,text="NO",style="MyButton.TButton",
            command=lambda:self.probabilidad_automatica(frasetxt.get()))
        btncalcularsinprob.place(x=230,y=160)

        btncallimpiar = ttk.Button(self.frmShanonFanon,text="Limpiar",style="MyButtonL.TButton",
            command=lambda:self.limpiar())
        btncallimpiar.place(x=145,y=200)
        

class principal_shanonF():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificacion Shanon Fanon")
        barra_menu = Menu(root)
        root.config(menu=barra_menu)

        ayudatr=Menu(barra_menu,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:Interfaz_ShanonF.creador(self))
        Inicio = Menu(barra_menu,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barra_menu,tearoff=0)
        Canal.add_command(label="Huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
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
        

        s1 = Interfaz_ShanonF(root)
        s1.pantalla()
        root.mainloop()


#probabilidad = [[20/50,'B'],[5/50,'A'],[4/50,'D'],[4/50,'F'],[4/50,'I'],[3/50,'E'],[3/50,'G'],[2/50,'H'],[2/50,'J'],[2/50,'K'],[1/50,'C']]
#probabilidad = [[6/34,'E'],[4/34,'A'],[4/34,'C'],[3/34,'L'],[3/34,'S'],[2/34,'T'],[2/34,'O'],[2/34,'M'],[2/34,'U'],[2/34,'N'],[2/34,'I'],[1/34,'D'],[1/34,'G']]
# probabilidad = [[0.32,'A'],[0.16,'R'],[0.12,'L'],[0.08,'D'],[0.08,'B'],[0.08,'E'],[0.08,'O'],[0.08,'Z']]
# h = shanon_fanon(probabilidad)
# h.shanon_f()

# ps = principal_shanonF()
# ps.iniciar()