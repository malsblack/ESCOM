#Escuela Superior de Computo
#Alumnos:
#Martinez Lopez Sebastian
#Ramirez Resendiz Luis Roque
#Materia: Analisis de Algoritmos
#Profesor: Luna Benoso Benjamin
#Practica 1:
#Determinacion experimental
#de la complejidad temporal
#de un algoritmo
#Fecha: 07/09/2022

import csv
import random

def core(ct,N):
    ct+=1 
    A=[0] 
    ct+=1
    A1=[] 
    ct+=1
    A2=[]
    ct+=1
    #for i in range(N-1): 
        #ct+=1
        #Elemento=random.randint(0,3*N)
        #A.append(Elemento)
        #ct+=1
        #ct+=1

    ct+=1
    for i in range(0,int(len(A)/2)):
        ct+=1
        A1.append(A[i])
        ct+=1

    ct+=1
    for i in range(int(len(A)/2),int(len(A))):
        ct+=1
        A2.append(A[i])
        ct+=1

    ct+=1
    for i in A1:
        ct+=1
        if i in A2:
            ct+=1
            indice1=A1.index(i)
            ct+=1
            indice2=A2.index(i)
            ct+=1
            indice3=indice2 + int(N/2)
            ct+=1
            return (ct)
    ct+=1
    return(ct)
N=0
coordenadas=[]

for i in range(50):
    N+=10
    ct=0
    dato=(N,core(ct,N))
    coordenadas.append(dato)

with open('Datos_practica_1.csv', 'w', newline="") as datos_grafica:
    csvwriter = csv.writer(datos_grafica)
    csvwriter.writerows(coordenadas)