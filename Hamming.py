import math 
import numpy as np

class Hamming():
    def __init__(self):
        pass

    def hamming_fun(self,codigo):
        mensaje = codigo
        tam = len(mensaje)
        binario_tam = bin(tam)
        t = len(binario_tam)
        binario_tam = binario_tam[2:t]
        cantidad_paridades = len(binario_tam)
        pos_paridades = []
        men = []
        for i in range(tam):
            men.append(mensaje[i])

        for i in range(cantidad_paridades):
            pp = (2**i)
            pos_paridades.append(pp)
            men.insert(pp-1,"p")
        
        #crear la matriz de paridades con contador
        mat_paridades=[[] for i in range(len(pos_paridades))]
        chequeo = []
        ver = True

        for f in range(len(mat_paridades)):
            if f>0:
                conta = 1
                ver = False
            else:
                conta = 0
                ver = True
            for c in range(len(men)):
                if ver:
                    l = str(men[c])
                    mat_paridades[f].append(l)
                    conta += 1 
                    if conta == pos_paridades[f]:
                        conta = 0
                        ver = False
                else:
                    l = "-"
                    mat_paridades[f].append(l)
                    conta += 1
                    if conta == pos_paridades[f]:
                        conta = 0
                        ver = True
                               
        for f in range(len(mat_paridades)):
            num_unos =0
            paridad = 2**f
            for c in range(len(men)):
                if mat_paridades[f][c] == "1":
                    num_unos+=1
            if num_unos%2 == 0:
                p = "0"
                mat_paridades[f][paridad-1] = p
                men[paridad-1] = p
            else:
                p = "1"
                mat_paridades[f][paridad-1] = p
                men[paridad-1] = p

        for h in range(len(chequeo)):
            num_unos =0
            for c in range(len(men)):
                if mat_paridades[h] == "1":
                    num_unos+=1
            if num_unos%2 == 0:
                p = "0"
                chequeo.append(p)
            else:
                p = "1"
                chequeo.append(p)
        
        mensaje_final = ""
        for i in range(len(men)):
            mensaje_final += men[i]
        
        return mensaje_final

            
# men = "1010001101"
# x = Hamming(men)
# x.hamming_fun()