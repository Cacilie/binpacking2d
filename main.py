from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter

ancho_del_telon = 24
renglones = []
piezas = []
telas = []
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

for pieza in piezas:
    telas.append(Tela(int(pieza.getalto()), ancho_del_telon))

piezas.sort(key=attrgetter("area"), reverse=True)

print("Piezas\n")


'''
for pieza in piezas:
    for tela in telas:
        if pieza.getancho() <= tela.getlibre() and pieza.getalto() <= tela.getaltura() and pieza.getasignada() is False:
            pieza.setasignada()
            tela.coser(pieza.getid())
            tela.setusado(pieza.getancho())
'''

contador = 0
i_pieza = 0
i_tela = 0
while i_pieza < len(piezas):
    if piezas[i_pieza].getancho() <= telas[i_tela].getlibre() and piezas[i_pieza].getalto() <= telas[i_tela].getaltura() and piezas[i_pieza].getasignada() is False:
        piezas[i_pieza].setasignada()
        telas[i_tela].coser(piezas[i_pieza].getid())
        telas[i_tela].setusado(piezas[i_pieza].getancho())
        i_pieza += 1
    else:
        i_tela += 1
        if i_tela == len(piezas):
            telas.append(Tela(int(piezas[i_pieza].getancho()), ancho_del_telon))


print("\nTelas\n")

altura_total_si = 0

for tela in telas:
    print(tela.tostring())
    if tela.getcosidos() != []:
        altura_total_si += tela.getaltura()

print("\n")
print("La altura del telón fue de " + str(altura_total_si) + " Unidades  ")
