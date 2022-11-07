
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

import random
import csv

def euclides(A,B):
    ct=0
    while B>0:
        ct+=1
        ct+=1
        R=A%B
        ct+=1
        A=B
        ct+=1
        B=R
        ct+=1
        
    return ct


A=10

coordenadas =[]
for i in range(5):
    A+=10
    for i in range(100):
        B=random.randint(0,A)
        dato=(A,euclides(A,B),B)
        coordenadas.append(dato)

with open('Datos_practica_1eu.csv', 'w', newline="") as datos_grafica:
    csvwriter = csv.writer(datos_grafica)
    csvwriter.writerows(coordenadas)
