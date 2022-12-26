def palabras(fichero):
    palabra=[]
    for i in fichero:
        palabra.append(i)

    return palabra

fichero1=open('archivo1.txt','r')
fichero2=open('archivo2.txt','r')

palabra1=palabras(fichero1)
palabra2=palabras(fichero2)
print(palabra1)
print(palabra2)
