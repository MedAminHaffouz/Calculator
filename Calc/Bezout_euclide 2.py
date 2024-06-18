a=int(input("Donner a : "))
b=int(input("Donner b : "))

Val_p=[0,1]
Val_r=[a,b]
Val_q=["(x)"]
Val_u=[1,0]
Val_v=[0,1]
p=1
Val_q.append(a//b)
r=Val_r[p]
while r!=0 :
    p=p+1
    Val_p.append(p)
    Val_r.append(Val_r[p-2]%Val_r[p-1])
    r=Val_r[p]
    if r==0:
        Val_q.append("(x)")
    else :
        Val_q.append(Val_r[p-2]//Val_r[p-1])
        u_p=Val_u[p-2]-(Val_q[p-1]*Val_u[p-1])
        Val_u.append(u_p)
        v_p=Val_v[p-2]-(Val_v[p-1]*Val_v[p-1])
        Val_v.append(v_p)

print(Val_p)
print(Val_r)
print(Val_q)
print(Val_u)
print(Val_v)
    
print("Solutions are : ")
print("u=("+str(Val_u[p-2])+")+("+str(Val_u[p-1])+str(")*k"))
print("v=("+str(Val_v[p-2])+")+("+str(Val_v[p-1])+str(")*k"))
print("for k a relative integer")