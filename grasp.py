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
    ids_seleccionados = [] # IDs que ya han sido seleccionados para formar parte de una solución
    lista_areas = [p.getarea() for p in l_piezas]
    menor = max(lista_areas)
    mayor = max(lista_areas)
    menor_id = 0
    cce = 0
    cmin = 0
    alfa = 0.5
    while len(ids_seleccionados) < len(l_piezas):
        posibles_agregar = []
        menor  = max(lista_areas)
        for p in l_piezas:
            if p.getarea() <= menor and p.getid() not in ids_seleccionados:
                menor_id = p.getid()
                cmin = p.getarea()
        # ids_seleccionados.append(menor_id)
        cce = cmin + (alfa * ( mayor - cmin))
        for p in l_piezas:
            if p.getarea() >= cmin and p.getarea() <= cce and p.getid() not in ids_seleccionados:
                posibles_agregar.append(p.getid())
        if posibles_agregar == []:
            for p in l_piezas:
                if p.getid() not in ids_seleccionados:
                    posibles_agregar.append(p.getid())
        eleccion = random.randrange(len(posibles_agregar))
        ids_seleccionados.append(posibles_agregar[eleccion])

    print(str(ids_seleccionados))
