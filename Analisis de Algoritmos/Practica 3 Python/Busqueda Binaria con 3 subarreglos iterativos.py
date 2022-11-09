import os
import random
ct=0
ct+=1
Arreglo_auxiliar=[]
ct+=1
Arreglo=[]
ct+=1
A=[]
ct+=1
B=[]
ct+=1
C=[]
ct+=1
n=90
ct+=1
for i in range(n):
    ct+=1
    dato=random.randint(0,n)
    ct+=1
    Arreglo.append(dato)
ct+=1
Arreglo.sort()
ct+=1
Arreglo_auxiliar=Arreglo
ct+=1
numero=int(input("Ingresar el numero a buscar:\n"))
ct+=1
while True:
    ct+=1
    ct+=1
    tamaño=int(len(Arreglo)/3)
    ct+=1
    print(Arreglo)
    ct+=1
    for i in range(tamaño):
        ct+=1
        A.append(Arreglo[i])
        ct+=1
        B.append(Arreglo[i+tamaño])
        ct+=1
        C.append(Arreglo[i+2*tamaño])
    ct+=1
    if numero<=A[len(A)-1]:
        ct+=1
        if numero in A:
            ct+=1
            if numero==A[len(A)-1]:
                ct+=1
                print("Su posicion esta en: {}\n".format(Arreglo_auxiliar.index(numero+1)))
                break
            else:
                ct+=1
                Arreglo=A
                ct+=1
                A=[]
                ct+=1
                B=[]
                ct+=1
                C=[]
                ct+=1
                continue
        else:
            ct+=1
            print("El numero no se encuentra en el arreglo")
            break
    ct+=1
    if numero>=B[len(B)-1]:
        ct+=1
        if numero in C:
            ct+=1
            if numero==B[len(B)-1]:
                ct+=1
                print("Su posicion esta en: {}\n".format(Arreglo_auxiliar.index(numero+1)))
                break
            else:
                ct+=1
                Arreglo=C
                ct+=1
                A=[]
                ct+=1
                B=[]
                ct+=1
                C=[]
                continue
        else:
            ct+=1
            print("El numero no se encuentra en el arreglo")
            break
    ct+=1
    if numero>A[len(A)-1] and numero<B[len(B)-1]:
        ct+=1
        if numero in B:
            ct+=1
            Arreglo=B
            ct+=1
            A=[]
            ct+=1
            B=[]
            ct+=1
            C=[]
            continue
        else:
            ct+=1
            print("El numero no esta en el arreglo")
            break
print(ct)