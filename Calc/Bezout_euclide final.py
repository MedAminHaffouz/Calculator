from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

from tabulate import tabulate
from numpy import *


def play():
    a=int(fen.a_input.text())
    b=int(fen.b_input.text())

    val_p=[0,1]
    val_r=[a,b]
    val_q=["(x)"]
    p=1
    val_q.append(a//b)
    while val_r[p]!=0:
        p=p+1
        val_p.append(p)
        val_r.append((val_r[p-2])%(val_r[p-1]))
        if val_r[p]!=0:
            val_q.append((val_r[p-1])//(val_r[p]))
        else :
            val_q.append("(x)")

    val_u=[1,0]
    val_v=[0,1]
    for i in range(2,p+1):
        val_u.append((val_u[i-2])-(val_q[i-1])*(val_u[i-1]))
        val_v.append((val_v[i-2])-(val_q[i-1])*(val_v[i-1]))
    
    L=p+2
    T=empty((5,L),dtype=object)

    T[0,0]="p"
    T[1,0]="r"
    T[2,0]="q"
    T[3,0]="u"
    T[4,0]="v"
    for j in range(1,L):
        T[0,j]=val_p[j-1]
        T[1,j]=val_r[j-1]
        T[2,j]=val_q[j-1]
        T[3,j]=val_u[j-1]
        T[4,j]=val_v[j-1]

    table = tabulate(T, headers='firstrow', tablefmt='pipe')
    
    fen.out.setText("solutions for the equation : "+str(a)+"*u+"+str(b)+"*v="+str(val_r[-2])+" are in form : ")
    fen.out_2.setText("u=("+str(val_u[p-1])+")+("+str(val_u[p])+str(")*k")+" and "+"v=("+str(val_v[p-1])+")+("+str(val_v[p])+str(")*k")+" , for k an integer")
    fen.output.setText(table)


app=QApplication([])
fen=loadUi("bezout_euclide.ui")
fen.show()
fen.play.clicked.connect(play)
app.exec_()