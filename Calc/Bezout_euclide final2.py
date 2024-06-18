from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import *


def play():
    a = int(fen.a_input.text())
    b = int(fen.b_input.text())

    val_p = [0, 1]
    val_r = [a, b]
    val_q = ["(x)"]
    p = 1
    val_q.append(a // b)
    while val_r[p] != 0:
        p = p + 1
        val_p.append(p)
        val_r.append((val_r[p - 2]) % (val_r[p - 1]))
        if val_r[p] != 0:
            val_q.append((val_r[p - 1]) // (val_r[p]))
        else:
            val_q.append("(x)")

    val_u = [1, 0]
    val_v = [0, 1]
    for i in range(2, p + 1):
        val_u.append((val_u[i - 2]) - (val_q[i - 1]) * (val_u[i - 1]))
        val_v.append((val_v[i - 2]) - (val_q[i - 1]) * (val_v[i - 1]))
    c = int(fen.b_input.text())
    gcd = val_r[-2]
    if c % gcd != 0:
        fen.output.setText("The equation " + str(a) + "u+" + str(b) + "v=" + str(c) + " admits no solutions")
    else:
        d = c // gcd
        u = "(" + str((val_u[-2]) * d) + ")+(" + str((val_u[-1]) * d) + ")*k"
        v = "(" + str((val_v[-2]) * d) + ")+(" + str((val_v[-1]) * d) + ")*k"
        fen.output.setText("The equation " + str(a) + "u+" + str(b) + "v=" + str(c) + " admits 2 solutions : ")
        aff = ""
        aff += (" u = " + u)
        aff += (" , v = " + v)
        aff += (" , for k an integer")
        fen.output_2.setText(aff)


app = QApplication([])
fen = loadUi("bezout_euclide2.ui")
fen.show()
fen.play.clicked.connect(play)
app.exec_()
