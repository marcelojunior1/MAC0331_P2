from geocomp.common import prim
from geocomp.common import segment
from geocomp.common import control
from geocomp import config
import math

# Constantes

X = 0
Y = 1


def Projeto2(l):
    print()

    filter_segments(l)
    mergesort(0,len(l), l, X)

    for x in range(len(l)):
        print(l[x])




# -------------------------------------------------------------------
# Garante que as extremidades de um segmento estejam ordenadas
# pela coordenada X. Efetua o processo para cada segmento da 
# lista 'l'.

def filter_segments (l):
    for i in range (len(l)):
        if (l[i].init.x > l[i].to.x):
            l[i].init, l[i].to = l[i].to, l[i].init
        elif (l[i].init.x == l[i].to.x):
            if (l[i].init.y > l[i].to.y):
                l[i].init, l[i].to = l[i].to, l[i].init


# -------------------------------------------------------------------
# Ordenada uma lista l[p...r-1] de segmentos pela coordenada 'init.x'

def mergesort(p, r, l, eixo):

    if (p < r-1):
        q = math.floor((p+r)/2)

        mergesort(p, q, l, eixo)
        mergesort(q, r, l, eixo)
        intercala(p, q, r, l, eixo)


def intercala(p, q, r, l, eixo):

    w = [None for i in range((r-p))] 

    for i in range(p, q):
        w[i-p] = l[i]

    for j in range(q, r):
        w[r-p+q-j-1] = l[j]
    
    i=0
    j=r-p-1

    for k in range(p, r):

        cond = False
        
        # Organizacao por X
        if eixo == X:
            cond =  (w[i].init.x < w[j].init.x) or (((w[i].init.x == w[j].init.x)) and w[i].init.y < w[j].init.y)
        else:
            print("Implementar se necessario")

        if (cond):
            l[k] = w[i]
            i+=1
        else:
            l[k] = w[j]
            j-=1


