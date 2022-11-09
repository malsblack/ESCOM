import time
def funcion(n,div,res,dd,q,r,ct):
    ct+=1
    ct+=1
    while dd<=n:
        ct+=1
        dd=2*dd
    ct+=1
    ct+=1
    while dd>div:
        ct+=1
        dd=dd/2
        ct+=1
        q=2*q
        ct+=1
        if(dd<=r):
            ct+=1
            r=r-dd
            ct+=1
            q=q+1
    return print(q,ct)

inicio=time.time()
ct=0
ct+=1
n=int(input("Valor de n:\n"))
ct+=1
div=int(input("Valor de div:\n"))
ct+=1
res=0
ct+=1
dd=div
ct+=1
q=0
ct+=1
r=n
ct+=1
funcion(n,div,res,dd,q,r,ct)
fin=time.time()
print(fin-inicio)
