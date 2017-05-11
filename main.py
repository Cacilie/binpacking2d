from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter
import grasp
import copy

ancho_del_telon = 90
renglones = []
piezas = []
telas = []
orden_solucion_i = []
nombre_instancia = input("Ingrese el nombre de la instancia \n")
archivo = open("Instancias/" + nombre_instancia + ".csv")
for linea in archivo.readlines():
    renglones.append(linea.rstrip("\n").split(","))

renglones.pop(0)
renglones.pop(0)
renglones.pop(0)
renglones.pop(0)
renglones.pop(0)

no_piezas = int(len(renglones))

i = 1
for pieza_info in renglones:
    nuevaPieza = Pieza(float(pieza_info[0]), float(pieza_info[1]), int(i))
    piezas.append(nuevaPieza)
    i += 1

piezas.sort(key=attrgetter("alto"), reverse=True)


def constructor(piezas_p):
    global ancho_del_telon
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
            telas_a.append(
                Tela(int(piezas_a[i_pieza].getalto()), ancho_del_telon))
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





telas = copy.deepcopy(constructor(piezas))
altura_total_si = 0

print("\nSolución Inicial\n")
for tela in telas:
    if tela.getcosidos() != []:
        altura_total_si += tela.getaltura()

mejor_solucion = altura_total_si
for pieza in piezas:
    orden_solucion_i.append(pieza.getid())

print("Mejor Solución conocida: " + str(mejor_solucion) + " Unidades de altura")
print("\nCon la distribucion\n")
for tela in telas:
    print(tela.getcosidos())

#movimientos

tela_movimiento = copy.deepcopy(movimientos(piezas, orden_solucion_i, mejor_solucion))

altura_movimiento = 0
for tela in tela_movimiento:
    altura_movimiento += tela.getaltura()


print("\nMejor Solución Encontrada\n")
if(altura_movimiento > 0):
    mejor_solucion = altura_movimiento

#grasp


grasp.InicializarGrasp(piezas)
grasp.cambiarStatusPiezas()
grasp.calcularPSoluciones()
resultadograsp = grasp.grasp(piezas, mejor_solucion)

if resultadograsp == -1:
    print("\nNo hubo mejora\n")
elif resultadograsp[1] == 0:
    print("\n" + str(resultadograsp[0])+ " Unidades de altura\n")
    print("\nCon la distribucion\n")
    comprobar_altura = 0
    for hilo in tela_movimiento:
        print(hilo.getcosidos())
        comprobar_altura += hilo.getaltura()
    print("COMPROBACION:: "+ str(comprobar_altura))
else:
     print("\n" + str(resultadograsp[0])+ " Unidades de altura\n")
     print("\nCon la distribucion\n")
     comprobar_altura = 0
     tela_movimiento = resultadograsp[1]
     for hilo in tela_movimiento:
         print(hilo.getcosidos())
         comprobar_altura += hilo.getaltura()
     print("COMPROBACION:: "+ str(comprobar_altura))
