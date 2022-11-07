#INSITUTO POLITECNICO NACIONAL
#ESCUELA SUPERIOR DE COMPUTO
#ANALISIS DE ALGORTIMOS
#PRACTICA 2: DETERMINACION EXPERIMENTAL DE LA COMPLEJIDAD TEMPORAL DE UN ALGORITMO
#FECHA 18/10/2022
#ALUMNOS: MARTINEZ LOPEZ SEBASTIAN
#         RAMIREZ REDENDIZ LUIS ROQUE

from calendar import c
import csv
ct=0
numeros_perfectos=[]
ct+=1   
def EsPerfecto(numero,ct):
    divisores=[] 
    ct+=1
    suma=0
    ct+=1
    salida=""
    ct+=1
    ct+=1
    for i in range(1,numero):
        ct+=1
        if (numero%i)==0:
            ct+=1
            divisores.append(i)
            ct+=1
    ct+=1
    for i in divisores:
        ct+=1
        suma=suma+i
        ct+=1
    ct+=1
    if suma==numero:
        ct+=1
        numeros_perfectos.append(numero)
        ct+=1
        salida="El numero {} es perfecto".format(numero)
        #return print(salida)
    else:
        ct+=1
        salida="El numero {} no es perfecto".format(numero)
        ct+=1
        return print(salida,ct)
        ct+=1
        
def MostrarPerfectos(n,ct):
    ct+=1
    m=1
    ct+=1
    ct+=1
    while(len(numeros_perfectos)<n):
        ct+=1
        EsPerfecto(m,ct)
        ct+=1
        ct+=1
        m+=1
        ct+=1
        if (len(numeros_perfectos)==n):
            ct+=1
            salida="Los numeros perfectos son {}".format(numeros_perfectos)
            ct+=1
            ct+=1
            return print(salida,ct)

    
ct+=1
MostrarPerfectos(int(input("Ingrese la cantidad de numeros perfectos: \n")),ct)
print(ct)