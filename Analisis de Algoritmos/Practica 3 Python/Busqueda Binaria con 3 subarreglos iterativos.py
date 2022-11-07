import os
import random
Arreglo=[]
A=[]
B=[]
C=[]
Bandera=True
n=30
for i in range(n):
    dato=random.randint(0,n)
    Arreglo.append(dato)

Arreglo.sort()
numero=int(input("Ingresar el numero a buscar:\n"))

while Bandera==True:
    tamaño=int(len(Arreglo)/3)
    print(Arreglo)
    print(A)
    print(B)
    print(C)
    for i in range(tamaño):
        A.append(Arreglo[i])
        B.append(Arreglo[i+tamaño])
        C.append(Arreglo[i+2*tamaño])

    if numero<=A[len(A)-1]:
        if numero in A:
            if numero==A[len(A)-1]:
                print("Su posicion esta en: {}\n".format(len(A)))
                Bandera==False
            else:
                Arreglo=A
                A=[]
                B=[]
                C=[]
                continue
        else:
            print("El numero no se encuentra en el arreglo")
            Bandera==False

    if numero>=B[len(B)-1]:
        if numero in C:
            if numero==B[len(B)-1]:
                print("Su posicion esta en: {}\n".format(len(A)+len(B)))
                Bandera==False
            else:
                Arreglo=C
                A=[]
                B=[]
                C=[]
                continue
        else:
            print("El numero no se encuentra en el arreglo")
            Bandera==False
    if numero>A[len(A)-1] and numero<B[len(B)-1]:
        if numero in B:
            Arreglo=B
            A=[]
            B=[]
            C=[]
            continue
        else:
            print("El numero no esta en el arreglo")
            Bandera==False
