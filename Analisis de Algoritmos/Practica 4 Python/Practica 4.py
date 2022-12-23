import cv2 #Para el procesamiento de la imagen
import numpy as np #Para la creacion y manipulacion de matrices
import pandas as pd #Para operaciones con matrices

def divideyvenceras(matriz,tamaño):
    if(tamaño!=2):
        partir=int(tamaño/2)
        A= matriz[0:partir,0:partir]
        print(A)
        B= matriz[0:partir,partir:tamaño]
        print(B)
        C= matriz[partir:tamaño,0:partir]
        print(C)
        D= matriz[partir:tamaño,partir:tamaño]
        print(D)
         divideyvenceras(A,int(len(A)))


    else:
        A=matriz[0:1,0:1]
        B=matriz[0:1,1:2]
        C=matriz[1:2,0:1]
        D=matriz[1:2,1:2]
        print(A[0])




    



















#Imagen=cv2.imread('imagen.bmp') #Se carga la imagen
#R=Imagen[:,:,0] #Se descompone la primer capa en Rojo
#G=Imagen[:,:,1] #Se descompone la primer capa en Verde
#B=Imagen[:,:,2] #Se descompone la primer capa en Azul
auxa=[]
#cv2.imshow('RGB',np.hstack([R,G,B])) #Se muestra la descomposicion de las image
prueba=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
prueba=np.array(prueba)

divideyvenceras(prueba,int(len(prueba)))
#divideyvenceras(R,int(len(R)))
#cv2.waitKey(0)
