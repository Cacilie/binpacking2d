from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter
import copy
import random

piezas_l = []  # Lista con el roden de las piezas
l_piezas = []  # Lista con los objetos de las piezas
p_soluciones = []


def InicializarGrasp(li_piezas):
    global piezas_l, l_piezas
    piezas_l = [x for x in range(1, len(li_piezas) + 1)]
    l_piezas = copy.deepcopy(li_piezas)
    l_piezas.sort(key=attrgetter("id"), reverse=False)


def returnListaPiezas():
    global piezas_l
    return piezas_l


def cambiarStatusPiezas():
    global l_piezas
    for p in l_piezas:
        p.setnoasignada()


def printPiezas():
    global l_piezas
    for p in l_piezas:
        print(p.tostring())

def calcularPSoluciones():
    global piezas_l, l_piezas, p_soluciones
    
