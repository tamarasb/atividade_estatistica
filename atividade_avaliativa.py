def moda(X,f):
    maior_f = 0;
    for x in f:
        if(x > maior_f):
            maior_f = x
    moda = X[f.index(maior_f)]
    return moda
    
def mediana(X, f):
    Fi = (somatorio(f))
    if((Fi % 2) == 0):
        med = int(Fi/2), int(Fi/2)+1
    else:
        med = Fi/2
    return med

def media(X,f):
    return somatorio_f(X, f)/somatorio(f)
      
def desvio(X,f):
    soma = 0
    for i in range(0, X.len()):
        soma += f[i]*pow(X[i]-media(X, f), 2)
        print(soma)
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
    p = (pos-somatorio(X[classe(X,h,pos)-1])*h/Fi)
    return p
 
def classe(X, h, pos):    
    index = 0
    for i in range(0, X.len):
        if(pos >= X[i] - h/2) and (pos <= X[i] + h/2):
            index = i
    return index

X = []
f = []

c = int(input("Quantidade de classes/F: "))
h = int(input("Amplitude: "))

# print("Xi")
# for i in range(0, c):
#     X.append(int(input("i: ")))

# print("\nFrequencia: ")
# for i in range(0, c):
#     f.append(int(input("i: "))

#Questão1
X = [350,450,550,650,750,850,950,1050,1150]
f = [14,46,58,76,68,62,48,22,6]

print("\nModa: "+str(moda(X,f)))
print("Mediana: "+str(mediana(X,f)))
print("Media: "+str(media(X,f)))
print("Desvio padrão: "+str(desvio(X,f)))
print("Percentil: "+str(percentil(X, f, h, 90)))