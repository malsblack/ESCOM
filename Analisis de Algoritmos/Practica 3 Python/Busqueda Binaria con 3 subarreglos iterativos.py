import os
import random
Arreglo_auxiliar=[]
Arreglo=[]
A=[]
B=[]
C=[]
n=30
for i in range(n):
    dato=random.randint(0,n)
    Arreglo.append(dato)

Arreglo.sort()
Arreglo_auxiliar=Arreglo
numero=int(input("Ingresar el numero a buscar:\n"))

while True:
    tamaño=int(len(Arreglo)/3)
    print(Arreglo)

    for i in range(tamaño):
        A.append(Arreglo[i])
        B.append(Arreglo[i+tamaño])
        C.append(Arreglo[i+2*tamaño])

    if numero<=A[len(A)-1]:
        if numero in A:
            if numero==A[len(A)-1]:
                print("Su posicion esta en: {}\n".format(Arreglo_auxiliar.index(numero+1)))
                break
            else:
                Arreglo=A
                A=[]
                B=[]
                C=[]
                continue
        else:
            print("El numero no se encuentra en el arreglo")
            break

    if numero>=B[len(B)-1]:
        if numero in C:
            if numero==B[len(B)-1]:
                print("Su posicion esta en: {}\n".format(Arreglo_auxiliar.index(numero+1)))
                break
            else:
                Arreglo=C
                A=[]
                B=[]
                C=[]
                continue
        else:
            print("El numero no se encuentra en el arreglo")
            break
    if numero>A[len(A)-1] and numero<B[len(B)-1]:
        if numero in B:
            Arreglo=B
            A=[]
            B=[]
            C=[]
            continue
        else:
            print("El numero no esta en el arreglo")
            break
