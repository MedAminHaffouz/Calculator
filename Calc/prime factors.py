n = int(input("Donner n : "))
A = 2
L = []
while n != 1:
    if n % A == 0:
        L.append(A)
        n = n // A
    else:
        A += 1
print(L)

S = ""
for i in range(len(L)):
    S += str(L[i]) + " * "
S = S[:len(S) - 2]
print(S)
