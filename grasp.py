from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter
import copy
import random

piezas_l = []  # Lista con el roden de las piezas
l_piezas = []  # Lista con los objetos de las piezas
p_soluciones = []
multiples_s = []
ancho_del_telon = 90
mejores_soluciones = [] # Contiene las mejores soluciones encontraas para cada posible solucion

def constructor(piezas_p):
    telas_a = []
    piezas_a = copy.deepcopy(piezas_p)
    i_pieza = 0
    i_tela = 0

    telas_a.append(Tela(int(piezas_a[0].getalto()), ancho_del_telon))
    while i_pieza < len(piezas_a):
        if piezas_a[i_pieza].getancho() <= telas_a[i_tela].getlibre() and piezas_a[i_pieza].getalto() <= telas_a[i_tela].getaltura() and piezas_a[i_pieza].getasignada() is False:
            piezas_a[i_pieza].setasignada()
            telas_a[i_tela].coser(piezas_a[i_pieza].getid())
            telas_a[i_tela].setusado(piezas_a[i_pieza].getancho())
            i_pieza += 1
        else:
            telas_a.append(Tela(int(piezas_a[i_pieza].getalto()), ancho_del_telon))
            i_tela += 1
            if i_tela == len(piezas_a):
                telas_a.append(
                    Tela(int(piezas_a[i_pieza].getancho()), ancho_del_telon))
    return telas_a

def movimientos(piezas_p, orden_inicial_p, mejor):
    piezas_a = copy.deepcopy(piezas_p)
    si_orden = copy.copy(orden_inicial_p)
    mejor_so = mejor
    mejor_orden = copy.copy(si_orden)
    m=0
    n=3
    sinmejora = 0
    mejor_tela = []
    while sinmejora < 1:
        for i in range(0, len(si_orden) - 4):
            mv_orden = []
            mv_piezas = []
            mv_tela = []
            mv_mejor = 0
            m = i
            n = i + 4
            aux1 = si_orden[:m]
            aux2 = si_orden[m:n]
            aux2.reverse()
            aux3 = si_orden[n:]
            mv_orden = list(aux1 + aux2 + aux3)

            for cord in mv_orden:
                for p in piezas_a:
                    if p.getid() == cord:
                        mv_piezas.append(p)

            mv_tela = constructor(mv_piezas)

            for t in mv_tela:
                mv_mejor += t.getaltura()

            if mv_mejor < mejor_so:
                si_orden = copy.copy(mv_orden)
                mejor_orden = copy.copy(mv_orden)
                mejor_so = mv_mejor
                mejor_tela = copy.deepcopy(mv_tela)
            else:
                si_orden = copy.copy(mv_orden)
                sinmejora += 1
    return mejor_tela

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
    global piezas_l, l_piezas, p_soluciones, multiples_s
    while len(multiples_s) < 200:
        # IDs que ya han sido seleccionados para formar parte de una solución
        ids_seleccionados = []
        lista_areas = [p.getarea() for p in l_piezas]
        menor = max(lista_areas)
        mayor = max(lista_areas)
        menor_id = 0
        cce = 0
        cmin = 0
        alfa = 0.000001
        while len(ids_seleccionados) < len(l_piezas):
            posibles_agregar = []
            for p in l_piezas:
                if p.getid() not in ids_seleccionados:
                    lista_areas.append(p.getarea())
            mayor = max(lista_areas)
            menor = max(lista_areas)
            for p in l_piezas:
                if p.getarea() <= menor and p.getid() not in ids_seleccionados:
                    menor_id = p.getid()
                    cmin = p.getarea()
            # print("Menor no asignado " + str(cmin))
            # ids_seleccionados.append(menor_id)
            cce = mayor - (alfa * (mayor - cmin))
            for p in l_piezas:
                if p.getarea() >= cmin and p.getarea() <= cce and p.getid() not in ids_seleccionados:
                    posibles_agregar.append(p.getid())
            if posibles_agregar == []:
                #print("no hay")
                for p in l_piezas:
                    if p.getid() not in ids_seleccionados and p.getarea() == cmin:
                        posibles_agregar.append(p.getid())
                '''
                for p in l_piezas:
                    if p.getid() not in ids_seleccionados:
                        posibles_agregar.append(p.getid())
                '''
            #print("posibles a agregar " + str(posibles_agregar))
            eleccion = random.randrange(len(posibles_agregar))
            ids_seleccionados.append(posibles_agregar[eleccion])
        # ids_seleccionados.reverse()
        multiples_s.append(ids_seleccionados)

def grasp(piezas_p, mejor_absoluto):
    global mejores_soluciones, multiples_s
    piezas_a = copy.deepcopy(piezas_p)
    piezas_ordenadas = []
    mejores_telas = []
    mejores_sumas = []
    mejor_absoluto = mejor_absoluto

    for ms in multiples_s:
        # print("\nMS\n")
        # print(ms)
        auxiliar = []
        for cord in ms:
            for p in piezas_a:
                if p.getid() == cord:
                    auxiliar.append(p)
        piezas_ordenadas.append(auxiliar)

    for lista in piezas_ordenadas:
        tela = constructor(lista)
        mejor_del_recibido = 0
        for hilo in tela:
            mejor_del_recibido += hilo.getaltura()
        mejores_soluciones.append(mejor_del_recibido)

    # print("Mejor antes de darle " + str(mejores_soluciones))
    for i in range(len(multiples_s)):
        tela_mejor_del_movimiento = movimientos(piezas_a, multiples_s[i], mejores_soluciones[i])
        mejores_telas.append(tela_mejor_del_movimiento)
        mejor_mv = 0
        for h in tela_mejor_del_movimiento:
            mejor_mv += h.getaltura()
        mejores_sumas.append(mejor_mv)

    # print("Mejores sumas " + str(mejores_sumas))
    mejor_de_mejores_suma = max(mejores_sumas)
    indice_mejor = -1
    for i in range(len(mejores_sumas)):
        if mejores_sumas[i] < mejor_de_mejores_suma and mejores_sumas[i] > 0 and mejores_sumas[i] < mejores_soluciones[i]:
            mejor_de_mejores_suma = mejores_sumas[i]
            indice_mejor = i
    if indice_mejor == -1:
        return -1
    else:
        if mejor_de_mejores_suma < mejor_absoluto:
            tela_mejor_de_mejores = mejores_telas[indice_mejor]
            return [mejor_de_mejores_suma, tela_mejor_de_mejores]
        else:
            return [mejor_absoluto, 0]



    # movimientos(piezas_p, orden_inicial_p, mejor)
