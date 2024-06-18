from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from math import *

def on():
    fen.output.setText("0")

def input1():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("1")
        else :
            S=fen.output.text()
            S+="1"
            fen.output.setText(S)

def input2():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("2")
        else :
            S=fen.output.text()
            S+="2"
            fen.output.setText(S)

def input3():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("3")
        else :
            S=fen.output.text()
            S+="3"
            fen.output.setText(S)

def input4():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("4")
        else :
            S=fen.output.text()
            S+="4"
            fen.output.setText(S)
            
def input5():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("5")
        else :
            S=fen.output.text()
            S+="5"
            fen.output.setText(S)

def input6():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("6")
        else :
            S=fen.output.text()
            S+="6"
            fen.output.setText(S)
            
def input7():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("7")
        else :
            S=fen.output.text()
            S+="7"
            fen.output.setText(S)
            
def input8():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("8")
        else :
            S=fen.output.text()
            S+="8"
            fen.output.setText(S)
            
def input9():
    if (fen.output.text())!="":
        if (fen.output.text())=="0" :
            fen.output.setText("")
            fen.output.setText("9")
        else :
            S=fen.output.text()
            S+="9"
            fen.output.setText(S)

def input0():
    if (fen.output.text())!="":
        if (fen.output.text())!="0" :
            S=fen.output.text()
            S+="0"
            fen.output.setText(S)

def add():
    if (fen.output.text())!="":
        S=fen.output_2.text()
        C=fen.output.text()
        if S!="" and S[-1]=="=":
            fen.output_2.clear()
            fen.output_2.setText(C+"+")
            fen.output.setText("0")
        if S!="" and (not("0"<=S[-1]<="9") and not(S[-1]=="=")):
            fen.output_2.setText(S+"+")
        else :
            N1=fen.output.text()
            Out=fen.output_2.text()
            fen.output_2.setText(Out+N1+"+")
            fen.output.setText("0")
        
def minus():
    if (fen.output.text())!="":
        S=fen.output_2.text()
        C=fen.output.text()
        if S!="" and S[-1]=="=":
            fen.output_2.clear()
            fen.output_2.setText(C+"-")
            fen.output.setText("0")
        if S!="" and (not("0"<=S[-1]<="9") and not(S[-1]=="=")):
            fen.output_2.setText(S+"-")
        else :
            N1=fen.output.text()
            Out=fen.output_2.text()
            fen.output_2.setText(Out+N1+"-")
            fen.output.setText("0")

def multiply():
    if (fen.output.text())!="":
        S=fen.output_2.text()
        C=fen.output.text()
        if S!="" and S[-1]=="=":
            fen.output_2.clear()
            fen.output_2.setText(C+"*")
            fen.output.setText("0")
        if S!="" and (not("0"<=S[-1]<="9") and not(S[-1]=="=")):
            fen.output_2.setText(S+"*")
        else :
            N1=fen.output.text()
            Out=fen.output_2.text()
            fen.output_2.setText(Out+N1+"*")
            fen.output.setText("0")
    
def divide():
    if (fen.output.text())!="":
        S=fen.output_2.text()
        C=fen.output.text()
        if S!="" and S[-1]=="=":
            fen.output_2.clear()
            fen.output_2.setText(C+"/")
            fen.output.setText("0")
        if S!="" and (not("0"<=S[-1]<="9") and not(S[-1]=="=")):
            fen.output_2.setText(S+"/")
        else :
            N1=fen.output.text()
            Out=fen.output_2.text()
            fen.output_2.setText(Out+N1+"/")
            fen.output.setText("0")
        
def equal():
    if (fen.output.text())!="":
        Out=fen.output_2.text()
        if "0"<=Out[-1]<="9" or Out[-1]==")":
            N=""
        else :
            N=fen.output.text()
        fen.output_2.setText(Out+N+"=")
        fen.output.setText("0")
        S=fen.output_2.text()
        S=S[:len(S)-1]
        A=eval(S)
        fen.output.setText(str(A))

def back():
    if fen.output.text()!="0":
        S=fen.output.text()
        S=S[:len(S)-1]
        fen.output.setText(S)
        if fen.output.text()=="":
            fen.output.setText("0")
    else :
        S=fen.output_2.text()
        S=S[:len(S)-1]
        fen.output_2.setText(S)

def parop():
    S=fen.output_2.text()
    if S!="" and not("0"<=S[-1]<="9"):
        fen.output_2.setText(S+"(")

def parcl():
    S=fen.output_2.text()
    if S!="" and not("0"<=S[-1]<="9") and S[-1]!="(" and S.find("(")!=-1:
        A=fen.output.text()
        fen.output_2.setText(S+A+")")
        fen.output.setText("0")
        
def comma():
    S=fen.output.text()
    S+="."
    fen.output.setText(S)
    
def sin():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="sin("
    fen.output_2.setText(S)

def cos():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="cos("
    fen.output_2.setText(S)
    
def tan():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="tan("
    fen.output_2.setText(S)
    
def asin():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="asin("
    fen.output_2.setText(S)
    
def acos():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="acos("
    fen.output_2.setText(S)
    
def atan():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="atan("
    fen.output_2.setText(S)
    
def sqrt():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="sqrt("
    fen.output_2.setText(S)
    
def absolute():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="abs("
    fen.output_2.setText(S)
    
def ln():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="log("
    fen.output_2.setText(S)
    
def e():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="e"
    fen.output_2.setText(S)
    
def pi():
    S=fen.output_2.text()
    if (len(S)!=0) and ("0"<=S[-1]<="9"):
        S+=""
    else :
        S+="pi"
    fen.output_2.setText(S)
    
def power():
    if (fen.output.text())!="":
        S=fen.output_2.text()
        C=fen.output.text()
        if S!="" and S[-1]=="=":
            fen.output_2.clear()
            fen.output_2.setText(C+"**")
            fen.output.setText("0")
        if S!="" and (not("0"<=S[-1]<="9") and not(S[-1]=="=")):
            fen.output_2.setText(S+"**")
        else :
            N1=fen.output.text()
            Out=fen.output_2.text()
            fen.output_2.setText(Out+N1+"**")
            fen.output.setText("0")

def sc_mode():
    fen.resize(580,355)
    fen.sin.setVisible(True)
    fen.cos.setVisible(True)
    fen.tan.setVisible(True)
    fen.sqrt.setVisible(True)
    fen.pow.setVisible(True)
    fen.asin.setVisible(True)
    fen.acos.setVisible(True)
    fen.atan.setVisible(True)
    fen.abs.setVisible(True)
    fen.e.setVisible(True)
    fen.ln.setVisible(True)
    fen.pi.setVisible(True)
    fen.sc_mode_frame.setVisible(True)
    fen.sin.clicked.connect(sin)
    fen.cos.clicked.connect(cos)
    fen.tan.clicked.connect(tan)
    fen.sqrt.clicked.connect(sqrt)
    fen.pow.clicked.connect(power)
    fen.asin.clicked.connect(asin)
    fen.acos.clicked.connect(acos)
    fen.atan.clicked.connect(atan)
    fen.abs.clicked.connect(absolute)
    fen.e.clicked.connect(e)
    fen.ln.clicked.connect(ln)
    fen.pi.clicked.connect(pi)

def norm_mode():
    fen.resize(418,355)
    fen.sin.setVisible(False)
    fen.cos.setVisible(False)
    fen.tan.setVisible(False)
    fen.sqrt.setVisible(False)
    fen.pow.setVisible(False)
    fen.asin.setVisible(False)
    fen.acos.setVisible(False)
    fen.atan.setVisible(False)
    fen.abs.setVisible(False)
    fen.e.setVisible(False)
    fen.ln.setVisible(False)
    fen.pi.setVisible(False)
    fen.sc_mode_frame.setVisible(False)

app=QApplication([])
fen=loadUi("gui_calculator.ui")
fen.show()
fen.output_2.setText("")
fen.resize(418,355)
fen.actionScientific_Mode.triggered.connect(sc_mode)
fen.actionNormal_Mode.triggered.connect(norm_mode)
fen.on_c_button.clicked.connect(on)
fen.sin.setVisible(False)
fen.cos.setVisible(False)
fen.tan.setVisible(False)
fen.asin.setVisible(False)
fen.acos.setVisible(False)
fen.atan.setVisible(False)
fen.sqrt.setVisible(False)
fen.pow.setVisible(False)
fen.abs.setVisible(False)
fen.e.setVisible(False)
fen.ln.setVisible(False)
fen.pi.setVisible(False)
fen.sc_mode_frame.setVisible(False)
fen.input_1.clicked.connect(input1)
fen.input_2.clicked.connect(input2)
fen.input_3.clicked.connect(input3)
fen.input_4.clicked.connect(input4)
fen.input_5.clicked.connect(input5)
fen.input_6.clicked.connect(input6)
fen.input_7.clicked.connect(input7)
fen.input_8.clicked.connect(input8)
fen.input_9.clicked.connect(input9)
fen.input_0.clicked.connect(input0)
fen.par_op.clicked.connect(parop)
fen.par_cl.clicked.connect(parcl)
fen.input_comma.clicked.connect(comma)
fen.add.clicked.connect(add)
fen.minus.clicked.connect(minus)
fen.multiply.clicked.connect(multiply)
fen.divide.clicked.connect(divide)
fen.equal.clicked.connect(equal)
fen.back.clicked.connect(back)
app.exec_()