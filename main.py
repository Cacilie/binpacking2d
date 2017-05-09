from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter
import grasp

ancho_del_telon = 24
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

piezas.sort(key=attrgetter("area"), reverse=True)


i_pieza = 0
i_tela = 0

telas.append(Tela(int(piezas[0].getalto()), ancho_del_telon))
while i_pieza < len(piezas):
    if piezas[i_pieza].getancho() <= telas[i_tela].getlibre() and piezas[i_pieza].getalto() <= telas[i_tela].getaltura() and piezas[i_pieza].getasignada() is False:
        piezas[i_pieza].setasignada()
        telas[i_tela].coser(piezas[i_pieza].getid())
        telas[i_tela].setusado(piezas[i_pieza].getancho())
        i_pieza += 1
    else:
        telas.append( Tela(int(  piezas[i_pieza].getalto()  ), ancho_del_telon)  )
        i_tela += 1
        if i_tela == len(piezas):
            telas.append(
                Tela(int(piezas[i_pieza].getancho()), ancho_del_telon))


altura_total_si = 0

print("Solución\n")
for tela in telas:
    print(tela.tostring())
    if tela.getcosidos() != []:
        altura_total_si += tela.getaltura()

mejor_solucion = altura_total_si
for pieza in piezas:
    orden_solucion_i.append(pieza.getid())

print("Mejor Solución conocida: " + str(mejor_solucion))
print("\nCon el orden: " + str(orden_solucion_i))

grasp.InicializarGrasp(piezas)
grasp.cambiarStatusPiezas()

#print("\nPiezas Grasp\n")
#grasp.printPiezas()

print("\nOtros Caminos\n")
grasp.calcularPSoluciones()
