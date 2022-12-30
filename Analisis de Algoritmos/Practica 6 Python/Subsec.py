a = open ('holamundo1.txt','r')
X = a.read()
a.close()

b = open ('holamundo2.txt','r')
Y = b.read()
b.close()

def tam(X,Y,m,n,encuentra):
    if m == 0 or n == 0:
        return 0

    key =(m,n)
    if key not in encuentra:

        if X[m-1]==Y[n-1]:
            encuentra[key]=tam(X,Y, m-1, n-1, encuentra)+1
        else:
            encuentra[key]=max(tam(X,Y,m,n-1,encuentra), tam(X,Y,m-1,n,encuentra))
    return encuentra[key]

if __name__ == '__main__':
 
 
    # crea un diccionario para almacenar soluciones a subproblemas
    encuentra = {}
 
    print('El tamaño de la subsecuencia comun es ', tam(X, Y, len(X), len(Y), encuentra))