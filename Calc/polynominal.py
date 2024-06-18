from math import sqrt
type=input("Give the degree of ur equation (1/2) : ")
if not(type=="1" or type=="2"):
    print("Error : press 1 for ax+b=0 equations and 2 for ax(^2)+bx+c=0 equations")
else :
    if type=="1":
        print("Equations type : ax+b=0")
        a=float(input("Give the a : "))
        b=float(input("Give the b : "))
        x=(-b)/a
        print("The solution for the equation "+str(a)+"x+"+str(b)+" is : "+str(x))
    else :
        print("Equations type : ax(^2)+bx+c=0")
        a=float(input("Give the a : "))
        b=float(input("Give the b : "))
        c=float(input("Give the c : "))
        D=b**2-4*a*c
        if D<0 :
            print("The equation has no solutions")
        elif D==0:
            x=(-b)/(2*a)
            print("The only solution for the equation "+str(a)+"x(^2)+"+str(b)+"x+"+str(c)+" is : "+str(x))
        else :
            x1=((-b)-sqrt(D))/(2*a)
            x2=((-b)+sqrt(D))/(2*a)
            print("The solutions for the equation "+str(a)+"x(^2)+"+str(b)+"x+"+str(c)+" are : "+str(x1)+" and "+str(x2))