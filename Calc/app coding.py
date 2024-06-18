from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_module import Ui_MainWindow

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

app = QApplication([])
fen = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(fen)

fen.show()
fen.output_2.setText("")
fen.on_c_button.clicked.connect(on)
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