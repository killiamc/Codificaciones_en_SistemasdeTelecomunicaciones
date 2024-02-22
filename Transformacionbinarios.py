from distutils.cmd import Command
import math 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import fd

import RLE as rle
import Huffman as hufman
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica
import pantalla_inicio as inicio
import Lineal as ln

class conversionbyd:
    def __init__(self,root) :
    #-------------barra TR---------------
        self.root = root
        self.frmtr = Frame()
        self.frmtr2 = Frame()
        
        self.inicio = StringVar()
        self.resultado = StringVar()
        self.numero = ""
        self.opcion = "binario"


    def transformacion(self,num):
        numero = ""
        i=1
        # parteentera = math.trunc(float(num))
        # partedecimal = float(num)-parteentera
        try:
            nume = abs(float(num))
        except ValueError:
            messagebox.showwarning("Conversor","Ingrese de nuevo el valor")
            self.inicio.set("")
            self.resultado.set("")
        tam = len(num)
        m = []
        m_2 = []
        s = 0
        pm = 0
        for t in num:
            s +=1 
            m.append(t)
            if t == ".":
                pm = s-1
            m_2 = m[pm:tam]        

        pd = ""
        pd = pd.join(m_2)

        parteentera = int(nume//1)
        if float(pd) > 1:
            partedecimal = 0
        else:
            partedecimal = float(pd)
        
        # parteentera = int(nume//1)
        # partedecimal = nume - parteentera
        
        var = True
        vardeci = True
        re = []
        while var:
            r = parteentera%2
            if parteentera//2 == 0:
                var = False
            else:
                var = True
            re.append(str(r))
            parteentera = parteentera//2
            i+=1
        re = list(reversed(re))
        numero=numero.join(re) 

        if partedecimal != 0.0:
            numero += "."
            while vardeci:
                rdeci = partedecimal*2
                pe = math.trunc(rdeci)
                partedecimal = rdeci-pe
                if partedecimal == 0.0:
                    vardeci = False
                else :
                    vardeci = True
                numero += str(pe)
        self.resultado.set(numero)
        numero = ""

    def a_decimal(self,num):

        try:
            nume = abs(float(num))
        except ValueError:
            messagebox.showwarning("Conversor","Ingrese de nuevo el valor")
            self.inicio.set("")
            self.resultado.set("")
        pm = 0
        s = 0
        total = 0
        s1=0
        pi = 0
        t = len(num)
        for j in num:
            s1+=1
            if j == ".":
                pm = s1
                pi += 1
                break
        

        r = t-pm+1
        
        if pm == 0:
            h = r-1
        else:
            h = t-r 
        print(h)
        for i in num:
            if pi == 1 or pi == 0:
                if i == "1" or i == "0" or i == ".":
                    if i != ".":
                        h-=1
                        print(h)
                        total += int(i)*pow(2,h)
                        self.resultado.set(total)
                else:
                    messagebox.showwarning("Conversor","Ingrese de nuevo el valor")
                    self.inicio.set("")
                    self.resultado.set("")
                    break
            else:
                messagebox.showwarning("Conversor","Ingrese de nuevo el valor")
                self.inicio.set("")
                self.resultado.set("")
   
    def creador(self):
        messagebox.showinfo("Autores","Daniela Sosa Y Killiam Puentes")

    def cambio(self,trans):
        global opcion
        opcion = trans
        s = ttk.Style()
        s.configure(
            "MyButton.TButton",
            foreground="darkturquoise",
            background="darkslategray",
        )   
        if opcion == "binario":
            self.resultado.set("")
            self.inicio.set("")
            self.frmtr.pack()
            self.frmtr.config(width="370",height="300",background="gray15",bd=10,relief="sunken")
            lbl = ttk.Label(self.frmtr,text="Ingrese el numero Decimal:",font=(36),foreground="deepskyblue")
            lbl.config(background="gray15")
            lbl.place(x=60,y=10)
            
            numerotxt = Entry(self.frmtr,textvariable=self.inicio,justify="center",background="lightsteelblue4",fg="turquoise1")
            numerotxt.place(x=25,y=50,width=300,height=50)
            
            btntransfroma = ttk.Button(self.frmtr,text="Transformación",style="MyButton.TButton",command=lambda:self.transformacion(numerotxt.get()))
            btntransfroma.place(x=130,y=120)

            rtatxt = Entry(self.frmtr,textvariable=self.resultado,justify="center",background="lightsteelblue4",fg="turquoise1")
            rtatxt.place(x=25,y=170,width=300,height=50)

            self.frmtr2.forget()
            print(opcion)
        elif opcion == "decimal":
            self.resultado.set("")
            self.inicio.set("")
            self.frmtr2.pack()
            self.frmtr2.config(width="370",height="300",background="gray15",bd=10,relief="sunken")

            lbl = ttk.Label(self.frmtr2,text="Ingrese el numero Binario:",font=(32),foreground="deepskyblue")
            lbl.config(background="gray15")
            lbl.place(x=60,y=10)

            numerotxt = Entry(self.frmtr2,textvariable=self.inicio,justify="center",background="lightsteelblue4",fg="turquoise1")
            numerotxt.place(x=25,y=50,width=300,height=50)

            btntransfroma = ttk.Button(self.frmtr2,text="Transformación",style="MyButton.TButton",command=lambda:self.a_decimal(numerotxt.get()))
            btntransfroma.place(x=130,y=120)

            rtatxt = Entry(self.frmtr2,textvariable=self.resultado,justify="center",background="lightsteelblue4",fg="turquoise1")
            rtatxt.place(x=25,y=170,width=300,height=50)

            self.frmtr.forget()
            print(opcion)


    #--------pantalla-------
    def pantalla(self):
        self.cambio("binario")
        
        

class principal_Transformacion():
    def iniciar(self):
        
        root = Tk()
        root.title("Transformacion")

        h = conversionbyd(root)
        barratransforma = Menu(root)
        root.config(menu=barratransforma)

        ayudatr=Menu(barratransforma,tearoff=0)
        ayudatr.add_command(label="Acerca de...",command=lambda:h.creador())

        opcionestr = Menu(barratransforma,tearoff=0)
        opcionestr.add_command(label="decimal a binario",command=lambda:h.cambio("binario"))
        opcionestr.add_command(label="binario a decimal",command=lambda:h.cambio("decimal"))
        
        Inicio = Menu(barratransforma,tearoff=0)
        Inicio.add_command(label="Inicio",command=lambda:[root.destroy(),inicio.principal_inicio.iniciar(self)])

        Canal = Menu(barratransforma,tearoff=0)
        Canal.add_command(label="huffman",command=lambda:[root.destroy(),hufman.principal_huffman.iniciar(self)])
        Canal.add_command(label="ShannonFannon",command=lambda:[root.destroy(),shannon.principal_shanonF.iniciar(self)])
        Canal.add_command(label="Aritmetica",command=lambda:[root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
        Canal.add_command(label="Algebraica",command=lambda:[root.destroy(),algebraica.principal_Algebraica.iniciar(self)])
                
        rLe = Menu(barratransforma,tearoff=0)
        rLe.add_command(label="RLE",command=lambda:[root.destroy(),rle.principal_RLE.iniciar(self)])
         
        Linear = Menu(barratransforma,tearoff=0)
        Linear.add_command(label="Lineal",command=lambda:[root.destroy(),ln.principal_Lineal.iniciar(self)])
         
        barratransforma.add_cascade(label="Opciones",menu=opcionestr)
        barratransforma.add_cascade(label="inicio",menu=Inicio)
        barratransforma.add_cascade(label="Cod.Canal",menu=Canal)
        barratransforma.add_cascade(label="RLE",menu=rLe)
        barratransforma.add_cascade(label="Cod.Lineal",menu=Linear)
        barratransforma.add_cascade(label="Ayuda",menu=ayudatr)
        

        h.pantalla()
        root.mainloop()

# h = principal_Transformacion()
# h.iniciar()