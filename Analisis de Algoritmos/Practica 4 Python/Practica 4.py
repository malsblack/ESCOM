import cv2 #Para el procesamiento de la imagen
import numpy as np #Para la creacion y manipulacion de matrices
import pandas as pd #Para operaciones con matrices

def divideyvenceras(lista):
    tamaño=len(lista)
    print(lista)
    if(tamaño!=1):
        validar=int(tamaño/2)
        aux=lista[0:validar]
        divideyvenceras(aux)
    else:
        nuevo_r.append(lista[0])











Imagen=cv2.imread('imagen.bmp') #Se carga la imagen
R=Imagen[:,:,0] #Se descompone la primer capa en Rojo
G=Imagen[:,:,1] #Se descompone la primer capa en Verde
B=Imagen[:,:,2] #Se descompone la primer capa en Azul
cv2.imshow('RGB',np.hstack([R,G,B])) #Se muestra la descomposicion de las image
cv2.waitKey(0)
nuevo_r=[]
for i in R:
    divideyvenceras(i)
print(nuevo_r)
print(len(nuevo_r))
pd.DataFrame(R).to_excel("R.xlsx") #Se escribe en un excel
pd.DataFrame(G).to_excel("G.xlsx")
pd.DataFrame(B).to_excel("B.xlsx")
