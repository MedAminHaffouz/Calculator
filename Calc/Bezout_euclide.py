from numpy import *

a = int(input("Donner a : "))
b = int(input("Donner b : "))
c = int(input("Donner c : "))

def PGCD(a,b):
    d=0
    while d==0:
        q=a//b
        r=a%b
        if (b%r==0):
            d=r
        else :
            a=b
            b=r
    return d

i=0
u=1
v=0
r=a*u+b*v
Val_r=[r]
Val_q=[0]
Val_u=[u]
Val_v=[v]

u=0
v=1
r=a*u+b*v
q=a//b

Val_r.append(r)
Val_q.append(q)
Val_u.append(u)
Val_v.append(v)

Find=False
while not(Find):
    r=Val_r[i] % Val_r[i-1]
    Val_r.append(r)
    i=i+1
    q=Val_r[i-1] // Val_r[i]
    Val_q.append(q)
    u=Val_u[i-2]-Val_q[i-1]*Val_u[i-1]
    v=Val_v[i-2]-Val_q[i-1]*Val_v[i-1]
    Val_u.append(u)
    Val_v.append(v)
    Find=(Val_r[i]==PGCD(a,b))

if Find:
    i=i+1
    r=0
    q=0
    u=Val_u[i-2]-Val_q[i-1]*Val_u[i-1]
    v=Val_v[i-2]-Val_q[i-1]*Val_v[i-1]
    Val_r.append(r)
    Val_q.append(q)
    Val_u.append(u)
    Val_v.append(v)

def arrays_screening(T):
    for i in range(len(T)):
        print(f"({i}) r={T[i]}, q={Val_q[i]}, u={Val_u[i]}, v={Val_v[i]}")

print("r, q, u, and v values are: ")
arrays_screening(Val_r)

n=i
print("Solutions for the equation are:")
print(f"u = {Val_u[n-2]} + k * {Val_u[n-1]}")
print(f"v = {Val_v[n-2]} + k * {Val_v[n-1]}")