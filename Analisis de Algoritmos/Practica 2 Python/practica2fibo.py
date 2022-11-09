#Escuela Superior de Computo
#Alumnos:
#Martinez Lopez Sebastian
#Ramirez Resendiz Luis Roque
#Materia: Analisis de Algoritmos
#Profesor: Luna Benoso Benjamin
#Practica 2:
#Determinacion experimental
#de la complejidad temporal
#de un algoritmo
#Fecha: /10/2022
ct=0
ct+=1
n=int(input("Introduce el valor de n: "))
ct+=1
a=0
ct+=1
b=1
ct+=1
for i in range(n):
        ct+=1
        print(a)
        ct+=1
        c=a+b
        ct+=1
        a=b
        ct+=1
        b=c      
        ct+=1
print("Contador",ct)