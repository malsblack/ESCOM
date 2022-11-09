import time
def funcion(n,div,ct):
    if div>n:
        ct+=1
        return 0
    else:
        ct+=1
        return print(1+funcion(n-div,div,ct))


inicio=time.time()
ct=0
ct+=1
n=int(input("Valor de n:\n"))
ct+=1
div=int(input("Valor de div:\n"))
ct+=1
funcion(n,div,ct)
fin=time.time()
print(fin-inicio)
