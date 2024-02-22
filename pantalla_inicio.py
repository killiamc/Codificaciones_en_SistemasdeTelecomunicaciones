
from tkinter import *
from tkinter import ttk
from traceback import FrameSummary
from turtle import color, fd
# import PIL.Image
# import PIL.ImageTk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import Transformacionbinarios as tr
import RLE as rle
import Huffman as huffman 
import Shanonfanon_Final as shannon
import Cod_Aritmetica as aritmetica
import Cod_algbraica as algebraica


class inicio_program():
    def __init__(self,root) :
        self.root = root
        pass

    def pantalla_lineal(self):
        s = ttk.Style()
        s.configure(
            "MyButtonL.TButton",
            foreground="orangered4",
        )
        
        self.frminicio_prog = Frame()
        self.frminicio_prog.pack()
        self.frminicio_prog.config(width="400",height="300",background="light steel blue",bd=10,relief="raised")

        posf = 0
        posc = 1
        lblin = ttk.Label(self.frminicio_prog,cursor="heart",text="Escoga la codificación",font=(48),foreground="midnightblue",justify=CENTER)
        lblin.config(background="light steel blue")
        lblin.grid(row=posf,column=posc,columnspan=2)

        img = mpimg.imread('imgcod.png')
        fig = Figure(figsize=(2,2),dpi=30)
        fig.add_subplot(111).imshow(img)

        canvas = FigureCanvasTkAgg(fig,master=self.frminicio_prog)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=1,columnspan=2)

        posf = 2
        posc = 1
        btntr = ttk.Button(self.frminicio_prog,text="Binario-Decimal",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),tr.principal_Transformacion.iniciar(self)])
        btntr.grid(row=posf,column=posc,padx=5,pady=5)

        posc = 2
        btnrle = ttk.Button(self.frminicio_prog,text="RLE",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),rle.principal_RLE.iniciar(self)])
        btnrle.grid(row=posf,column=posc,padx=5,pady=5)

        posf = 3
        posc = 1
        btnhuff = ttk.Button(self.frminicio_prog,text="Huffman",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),huffman.principal_huffman.iniciar(self)])
        btnhuff.grid(row=posf,column=posc,padx=5,pady=5)

        posc = 2
        btnshanon = ttk.Button(self.frminicio_prog,text="Shannon Fanon",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),shannon.principal_shanonF.iniciar(self)])
        btnshanon.grid(row=posf,column=posc,padx=5,pady=5)

        posf = 4
        posc = 1
        btnarit = ttk.Button(self.frminicio_prog,text="Aritmetica",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),aritmetica.principal_Aritmetica.iniciar(self)])
        btnarit.grid(row=posf,column=posc,padx=5,pady=5)

        posc = 2
        btnalge = ttk.Button(self.frminicio_prog,text="Algebraica",style="MyButton.TButton",
            command=lambda:[self.root.destroy(),algebraica.principal_Algebraica.iniciar(self)])
        btnalge.grid(row=posf,column=posc,padx=5,pady=5)

                

    
class principal_inicio():
    
    def iniciar(self):
        root = Tk()
        root.title("Codificaciones")
        
        s1 = inicio_program(root)
        s1.pantalla_lineal()
        root.mainloop()


x = principal_inicio()
x.iniciar()