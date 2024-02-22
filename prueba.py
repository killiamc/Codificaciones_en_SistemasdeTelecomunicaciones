from logging import root
import numpy as np

# import matplotlib.pyplot as plt

# from tkinter import * 

import random




# master = Tk()
# w = Canvas(master, width=250, height=200)
# w.pack()

# l=0
# w.create_rectangle(0, 0, 50, 5, fill="blue", outline = 'blue')
# w.create_rectangle(50, 0, 500, 5, fill="red", outline = 'blue')

# master.mainloop() 

# pru = "0.45"
# pruf = pru[1:len(pru)]
# print(pruf)







# x1 = np.linspace(-2, 0, num=3)

# x2 = np.linspace(0, 1, num=2)

# x3 = np.linspace(1, 3, num=3)

# x4 = np.linspace(3, 5, num=3)

 

# plt.plot(x1, [2 for x in x1], 'g',  label='y = 2, x en [-2, 0]')

# plt.plot(x2, [x + 2 for x in x2], 'b', label='y = x + 2, x en [0, 1]')

# plt.plot(x3, [.5 * x - 1.5 for x in x3], 'r', label='y = .5*x - 1.5, x en (1, 3]')

# plt.plot(1, -1, 'ro', markersize=5, fillstyle='none', markerfacecolor='w')

# plt.plot(x4, [.5 * x + 2.5 for x in x4], 'm', label='y = .5*x +2.5, x en (3, 5]')

# plt.plot(3, 4, 'mo', markersize=5, fillstyle='none', markerfacecolor='w')

 

# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',

#            ncol=2, mode="expand", borderaxespad=0.)

 

# plt.grid()

# plt.show()

num = 5
con = 1
# mat_i = []
# for f in range(num):
#     momen = []
#     for c in range(num):
#         momen.append(con)
#         con+=1
#     mat_i.append(momen)
# # mat = np.array(mat_i)
# # print(mat)

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
    else:
        canti = random.randrange(1, 11, 1)
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

mat = np.array(aleatoria)
print(mat)
rows=num
columns=num

# #crea la cantidad de listas 
# solution=[[] for i in range(rows+columns-1)]

# for i in range(rows):
#     for j in range(columns):
#         sum=i+j
#         if(sum%2 ==0):

#             #add at beginning
#             solution[sum].insert(0,mat[i][j])
#         else:

#             #add at end of the list
#             solution[sum].append(mat[i][j])
# print(solution)
# mensaje = ""
# for k in range(len(solution)):
#     for p in range(len(solution[k])):
#         mensaje += str(solution[k][p])

# print("zigzag"+mensaje,end="/n")
m1 = ""
for c in range(columns):
    for f in range(rows):
        m1 += str(mat[c][f])

print("horizonatl \n"+m1)
m2 = ""
for c in range(columns):
    for f in range(rows):
        m2 += str(mat[f][c])

print("vertical \n"+m2)


mensaje = m1
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
print(mat_rle)