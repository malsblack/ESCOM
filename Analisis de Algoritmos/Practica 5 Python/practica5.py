import random

dias_apertura = random.randint(1, 31)
duracionFert = random.randint(3, 13)
A=[0]
for i in range(dias_apertura):
    Elemento=random.randint(1,31)
    A.append(Elemento)
    A.sort()
diaprt=Elemento
ultimm=A[dias_apertura]
if duracionFert < diaprt:
    print ("No hay solucion")
elif duracionFert >= diaprt & duracionFert < diaprt:
    print ("El granjero va a la tienda este dia")
    print ("Duracion del fertilizante: ",duracionFert)
    print ("Dia de apertura: ",diaprt)
elif (ultimm):
    if duracionFert == ultimm:
       print ("El granjero va a la tienda el ultimo dia del mes")
diaprt+1
