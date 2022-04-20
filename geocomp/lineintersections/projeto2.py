# Arvore Rubro-negra baseada na implementacao do livro \
# Introduction to Algorithms - 3rd ed. - Cormen, Leiserson, Rivest & Stein (2009)

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
SEGM = 0
ESQ = 1


# -------------------------------------------------------------------
# Chamada da funcao

def Projeto2(l):
    print()
    for i in range(len(l)):
        print(i, l[i])

    filter_segments(l)

    Varredura(l)


# -------------------------------------------------------------------
# Executa a linha de varredura do algoritmo

def Varredura(l):
    # Cria a fila de eventos
    fila = []

    for i in range(len(l)):
        fila.append([i, True])
        fila.append([i, False])

    mergesort(0, len(fila), fila, l, X)

    arvore = RN(l)

    for i in range(len(fila)):
        print(i, fila[i])

    for i in range(len(fila)):
        intersecta = False
        segm_intersecta = []
        print(i)

        if fila[i][ESQ]:
            print("Insere: ", fila[i][SEGM])
            # Insere na arvore de busca
            arvore.put_op(fila[i][SEGM], -1)

            # Testa com o predecessor e sucessor
            #A, B = arvore.max_min_no(fila[i][SEGM])

            #print("INTER: ", A, B)

        else:
            print("Remove: ", fila[i][SEGM])
            # Remove e testa se os segmentos tem intercessao
            #A, B = arvore.max_min_no(fila[i][SEGM])
            #print("INTER: ", A, B)

            arvore.remove_op(fila[i][SEGM])

        arvore.print_tree_op()


    print("----------------------------------")
    #arvore.retorna_chave()


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

def Esquerda_plus(a: Point, b: Point, c: Point):
    return area2(a, b, c) > 0


def Esquerda( A: Segment, B: Segment):
    tmp = area2(A.init, A.to, B.init)

    if A.init.x < B.init.x:
        return not tmp > 0

    if tmp == 0:
        print("Ponto sobre outro segmento", A, B)

    return tmp >= 0


# Verifica se c esta no seguimento ab
def Entre(a: Point, b: Point, c: Point):
    if not collinear(a, b, c):
        return False

    if a.x is not b.x:
        return (a.x <= c.x <= b.x) or (b.x <= c.x <= a.x)
    else:
        return (a.y <= c.y <= b.y) or (b.y <= c.y <= a.y)


# Verifica se dois segmentos se intersectao
def Intersecta_prop(A: Segment, B: Segment):
    if collinear(A.init, A.to, B.init) or collinear(A.init, A.to, B.to) or \
            collinear(B.init, B.to, A.init) or collinear(B.init, B.to, A.to):
        return False

    return (Esquerda_plus(A.init, A.to, B.init) ^ Esquerda_plus(A.init, A.to, B.to) )and \
           (Esquerda_plus(B.init, B.to, A.init) ^ Esquerda_plus(B.init, B.to, A.to))


def Intersecta(A: Segment, B: Segment):
    if Intersecta_prop(A, B):
        print("OK")
        return True

    return Entre(A.init, A.to, B.init) or Entre(A.init, A.to, B.to) or \
           Entre(B.init, B.to, A.init) or Entre(B.init, B.to, A.to)


# -------------------------------------------------------------------
#

def mergesort(p, r, fila, l, eixo):
    if p < (r - 1):
        q = math.floor((p + r) / 2)

        mergesort(p, q, fila, l, eixo)
        mergesort(q, r, fila, l, eixo)
        intercala(p, q, r, fila, l, eixo)


def intercala(p, q, r, fila, l, eixo):
    w = [None for i in range((r - p))]

    for i in range(p, q):
        w[i - p] = fila[i]
    for j in range(q, r):
        w[r - p + q - j - 1] = fila[j]

    i = 0
    j = r - p - 1

    for k in range(p, r):
        cond = False

        # Organizacao por X
        if eixo == X:
            # cond = (w[i].init.x < w[j].init.x) or (((w[i].init.x == w[j].init.x)) and w[i].init.y < w[j].init.y)
            i_1 = w[i][SEGM]
            i_2 = w[j][SEGM]
            ori_1 = w[i][ESQ]
            ori_2 = w[j][ESQ]

            p1 = l[i_1].init if ori_1 else l[i_1].to
            p2 = l[i_2].init if ori_2 else l[i_2].to

            cond = (p1.x < p2.x)
        else:
            print("Implementar se necessario")

        if cond:
            fila[k] = w[i]
            i += 1
        else:
            fila[k] = w[j]
            j -= 1
