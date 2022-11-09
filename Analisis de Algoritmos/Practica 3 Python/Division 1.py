import time
inicio=time.time()
def funcion(n,div,res,q,ct):
    ct+=1
    ct+=1
    while n>=div:
        ct+=1
        n=n-div
        ct+=1
        q=q+1
        ct+=1
        res=n
        ct+=1
    fin=time.time()
    resultado=fin-inicio
    return print(ct,resultado)



ct=0
ct+=1
n=int(input("Valor de n:\n"))
ct+=1
div=int(input("Valor de div:\n"))
ct+=1
res=0
ct+=1
q=0
ct+=1
funcion(n,div,res,q,ct)
