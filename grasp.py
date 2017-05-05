from Classes.Pieza import Pieza
from Classes.Tela import Tela

piezas_l = []
l_piezas =[]
def crearPosiblesSoluciones(li_piezas):
    global piezas_l, l_piezas
    piezas_l = [ x for x in range(1, len(li_piezas) + 1)]
    l_piezas = [li_piezas[x] for x in range(len(li_piezas))]

def returnListaPiezas():
    global piezas_l
    return piezas_l

def printPiezas():
    global l_piezas
    for p in l_piezas:
        print(p.tostring())
