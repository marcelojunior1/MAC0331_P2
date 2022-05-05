""""
    Nome: Marcelo Nascimento
    NUSP: 11222012

"""
from random import randint, seed

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

    # Ordena a fila pela coordenada X
    mergesort(0, len(fila), fila, l, X)

    # Cria a arvore de segmentos
    arvore = RN(l)

    # Processa a fila de segmentos
    control.sleep()
    for i in range(len(fila)):
        intersecta = False

        segm_k = fila[i][SEGM]

        segmento = l[segm_k]
        x = 0
        if fila[i][ESQ]:
            x = segmento.init.x
        else:
            x = segmento.to.x

        linha = control.plot_vert_line(x, "white", 1)

        segm_intersecta = []
        segm_intersecta.append(l[segm_k])

        if fila[i][ESQ]:
            # Insere na arvore de busca
            arvore.put_op(fila[i][SEGM], None)

            A, B = arvore.max_min_no(segm_k)
            # print("Teste: ", A, B)

            # Testa com o predecessor e sucessor

            if A != -1 and not intersecta:
                l[segm_k].hilight(color_line="blue")
                l[A].hilight()
                control.sleep()

                intersecta = prim.intersect(l[A].init, l[A].to, l[segm_k].init, l[segm_k].to)
                if intersecta:
                    segm_intersecta.append(l[A])

                l[segm_k].plot()
                l[A].plot()

            if B != -1 and not intersecta:
                l[segm_k].hilight(color_line="blue")
                l[B].hilight()
                control.sleep()

                intersecta = prim.intersect(l[segm_k].init, l[segm_k].to, l[B].init, l[B].to)
                if intersecta:
                    segm_intersecta.append(l[B])

                l[segm_k].plot()
                l[B].plot()

        else:
            # Remove e testa se os segmentos tem intercessao
            A, B = arvore.max_min_no(fila[i][SEGM])

            if A != -1 and not intersecta:
                l[segm_k].hilight(color_line="blue")
                l[A].hilight()
                control.sleep()

                intersecta = prim.intersect(l[A].init, l[A].to, l[segm_k].init, l[segm_k].to)
                if intersecta:
                    segm_intersecta.append(l[A])

                l[segm_k].plot()
                l[A].plot()

            if B != -1 and not intersecta:
                l[segm_k].hilight(color_line="blue")
                l[B].hilight()
                control.sleep()

                intersecta = prim.intersect(l[segm_k].init, l[segm_k].to, l[B].init, l[B].to)
                if intersecta:
                    segm_intersecta.append(l[B])

                l[segm_k].plot()
                l[B].plot()

            arvore.remove_op(fila[i][SEGM])

        control.plot_delete(linha)

        if intersecta:
            segm_intersecta[0].hilight()
            segm_intersecta[1].hilight()
            break


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
# Ordena a fila pela coordenada X

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
            i_1 = w[i][SEGM]
            i_2 = w[j][SEGM]
            ori_1 = w[i][ESQ]
            ori_2 = w[j][ESQ]

            p1 = l[i_1].init if ori_1 else l[i_1].to
            p2 = l[i_2].init if ori_2 else l[i_2].to

            cond = (p1.x <= p2.x)

            # Caso sejam o mesmo segmento,
            # o ponto de inicio e inserido primeiro
            if i_1 == i_2:
                if ori_1:
                    cond = True
                else:
                    cond = False
        else:
            print("Implementar se necessario")

        if cond:
            fila[k] = w[i]
            i += 1
        else:
            fila[k] = w[j]
            j -= 1
