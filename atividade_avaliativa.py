def moda(X,f):
    maior_f = 0;
    for x in f:
        if(x > maior_f):
            maior_f = x
    moda = X[f.index(maior_f)]
    return moda
    
def mediana(X, f, h):
    Fi = (somatorio(f))
    if((Fi % 2) == 0):
        pos = int(Fi/2), int(Fi/2)+1
        med = (pos[0]+pos[1])/2
    else:
        pos = Fi/2
        med = pos
    return X[classe(f, h, med)]

def media(X,f):
    return somatorio_f(X, f)/somatorio(f)
      
def desvio(X,f):
    soma = 0
    for i in range(0, len(X)):
        soma += pow(X[i]-media(X, f), 2)
    S = (pow(soma, 1/2))/(somatorio(f)-1)
    return S
    
def somatorio(f):
    soma = 0
    for fi in f:
        soma += fi
    return soma

def somatorio_f(X,f):
    soma = 0
    for x in X:
        soma += f[X.index(x)]*x
    return soma

def percentil(X,f,h,i):
    Fi = somatorio(f)
    pos = i*Fi/100
    p = (pos-somatorio(X[0:classe(X,h,pos)-1])*h/Fi)
    return p
 
def classe(X, h, pos):    
    index = 0
    for i in range(0,len(X)):
        if(pos <= somatorio(X[0:i+1])):
            index = i
            break
    return index

def constroi_tabela(valores, c, h):
    X, f = [],[]

    l = valores[0]
    for i in range(0, c):
        X.append(l + h/2)
        l = X[i] + h/2
        f.append(0)
    
    for x in valores:
        for y in range(0, c):
            if (x >= X[y] - h/2) and (x < X[y] + h/2):
                f[y] += 1
    return (X,f)

def imprime_res(X,f,c,h):
    print("\nModa: "+str(moda(X,f)))
    print("Mediana: "+str(mediana(X,f,h)))
    print("Media: "+str(media(X,f)))
    print("Desvio padrão: "+str(desvio(X,f)))
    print("P15: "+str(percentil(X, f, h, 15)))
    print("P90: "+str(percentil(X, f, h, 90)))

#Questão1
X1 = [350,450,550,650,750,850,950,1050,1150]
f1 = [14,46,58,76,68,62,48,22,6]

c1 = 9 #Quantidade de classes
h1 = 100 #Amplitude
imprime_res(X1,f1,c1,h1)

#Questão2
V = [61,65,43,53,55,51,58,55,59,56,
     52,53,62,49,68,51,50,67,62,64,
     53,56,48,50,61,44,64,53,54,55,
     48,54,57,41,54,71,57,53,46,48,
     55,46,57,54,48,63,49,55,52,51]
V.sort()

c2 = 7
h2 = 5

X2,f2 = constroi_tabela(V, c2, h2)

imprime_res(X2,f2,c2,h2)