import os
import random

def Crear_numeros():
    for i in range(30):
        dato=random.randint(0,30)
        Arreglo.append(dato)
        Auxiliar.append(dato)
    Arreglo.sort()
    Auxiliar.sort()

def dividir_numeros(Arreglo,A,B,C):
    for i in range(int(len(Arreglo)/3)):
        A.append(Arreglo[i])
        B.append(Arreglo[i+(int(len(Arreglo)/3))])
        C.append(Arreglo[i+2*(int(len(Arreglo)/3))])


def Busqueda(Arreglo,Auxiliar,A,B,C):
    dividir_numeros(Arreglo,A,B,C)
    Bandera1=A[len(A)-1]
    Bandera2=B[len(B)-1]

    if numero in Auxiliar:
        if numero<=Bandera1:
            if numero==Bandera1:
                return(print("El numero esta en la posicion: {}\n".format(Auxiliar.index(numero+1))))
                
            else:
                dividir_numeros(Arreglo=A,A=[],B=[],C=[])

        if numero>=Bandera2:
            if numero==Bandera2:
                return(print("El numero esta en la posicion: {}\n".format(Auxiliar.index(numero+1))))
                
            else:
                dividir_numeros(Arreglo=C,A=[],B=[],C=[])

        if numero>Bandera1 and numero<Bandera2:
            dividir_numeros(Arreglo=B,A=[],B=[],C=[])

    else:
        return(print("EL numero no se encuentra dentro del arreglo\n"))
Arreglo=[]
Auxiliar=[]
A=[]
B=[]
C=[]
numero=int(input("Ingresar el numero a buscar:\n"))
Crear_numeros()
Busqueda(Arreglo=Arreglo,Auxiliar=Auxiliar,A=A,B=B,C=C)


