import random
import csv
def palabras(archivo):
    diccionario=["Hola","Adios","Carro","Ferrocarril","Cigarro"]
    archivo.write("{}\n".format(random.choice(diccionario)))
    archivo.close()

def abrir(archivo):
    palabra=archivo.read()
    archivo.close()
    return palabra

def tam(X,Y,m,n,encuentra):
    global ct
    ct+=1
    if m == 0 or n == 0:
        ct+=1
        ct+=1
        return 0
    ct+=1
    key =(m,n)
    ct+=1
    if key not in encuentra:
        ct+=1
        if X[m-1]==Y[n-1]:
            ct+=1
            encuentra[key]=tam(X,Y, m-1, n-1, encuentra)+1
        else:
            ct+=1
            encuentra[key]=max(tam(X,Y,m,n-1,encuentra), tam(X,Y,m-1,n,encuentra))
    ct+=1
    return encuentra[key]

coordenadas=[]

for i in range(50):

    a=open("holamundo1.txt","a")
    b=open("holamundo2.txt","a")
    palabras(a)
    palabras(b)
    ct=0
    a=open("holamundo1.txt","r")
    X=abrir(a)
    b=open("holamundo2.txt","r")
    Y=abrir(b)
    encuentra = {}
    
    subsec=(tam(X, Y, len(X), len(Y), encuentra),ct)
    print('El tamaño de la subsecuencia comun es {} y su contador es {}'.format(subsec[0],subsec[1]))
    coordenadas.append(subsec)

with open('Datos_practica_6.csv', 'w', newline="") as datos_grafica:
    csvwriter=csv.writer(datos_grafica)
    csvwriter.writerow(("Número de caracteres","Contador"))
    csvwriter.writerows(coordenadas)

