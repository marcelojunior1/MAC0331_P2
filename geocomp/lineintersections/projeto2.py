from geocomp.common import prim
from geocomp.common import segment
from geocomp.common import control
from geocomp import config
from geocomp.common.point import Point
from geocomp.common.prim import *
from geocomp.common.segment import Segment
from geocomp.rn import RN
import math

# Constantes
X = 0
Y = 1


# -------------------------------------------------------------------
# Chamada da funcao

def Projeto2(l):
    print()
    arvore = RN()

    filter_segments(l)
    mergesort(0, len(l), l, X)

    Varredura(l)

# -------------------------------------------------------------------
# Executa a linha de varredura do algoritmo

def Varredura(l):
    print("OK")

# -------------------------------------------------------------------
# Garante que as extremidades de um segmento estejam ordenadas
# pela coordenada X. Efetua o processo para cada segmento da
# lista 'l'.

def filter_segments(l):
    for i in range(len(l)):
        if (l[i].init.x > l[i].to.x):
            l[i].init, l[i].to = l[i].to, l[i].init
        elif (l[i].init.x == l[i].to.x):
            if (l[i].init.y > l[i].to.y):
                l[i].init, l[i].to = l[i].to, l[i].init


# -------------------------------------------------------------------
# Funcoes

# Verifica se c esta no seguimento ab
def Entre(a: Point, b: Point, c: Point):
    if not collinear(a, b, c):
        return False

    if a.x is not b.x:
        return (a.x <= c.x <= b.x) or (b.x <= c.x <= a.x)
    else:
        return (a.y <= c.y <= b.y) or (b.y <= c.y <= a.y)


# Verifica se dois segmentos se intersectao
def Intersecta(A: Segment, B: Segment):
    if collinear(A.init, A.to, B.init) or collinear(A.init, A.to, B.to) or \
            collinear(B.init, B.to, A.init) or collinear(B.init, B.to, A.to):
        return True

    return Entre(A.init, A.to, B.init) or Entre(A.init, A.to, B.to) or \
           Entre(B.init, B.to, A.init) or Entre(B.init, B.to, A.to)


# -------------------------------------------------------------------
# Ordenada uma lista l[p...r-1] de segmentos pela coordenada 'init.x'

def mergesort(p, r, l, eixo):
    if (p < r - 1):
        q = math.floor((p + r) / 2)

        mergesort(p, q, l, eixo)
        mergesort(q, r, l, eixo)
        intercala(p, q, r, l, eixo)


def intercala(p, q, r, l, eixo):
    w = [None for i in range((r - p))]

    for i in range(p, q):
        w[i - p] = l[i]

    for j in range(q, r):
        w[r - p + q - j - 1] = l[j]

    i = 0
    j = r - p - 1

    for k in range(p, r):

        cond = False

        # Organizacao por X
        if eixo == X:
            cond = (w[i].init.x < w[j].init.x) or (((w[i].init.x == w[j].init.x)) and w[i].init.y < w[j].init.y)
        else:
            print("Implementar se necessario")

        if (cond):
            l[k] = w[i]
            i += 1
        else:
            l[k] = w[j]
            j -= 1
