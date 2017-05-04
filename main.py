from Classes.Pieza import Pieza
from Classes.Tela import Tela
from operator import attrgetter

ancho_del_telon = 24;
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

piezas.sort(key=attrgetter("area"), reverse=True)


telas.append(Tela(int(piezas[0].getalto()), ancho_del_telon))

# Inicia constructivo
for pieza in piezas:
    for tela in telas:
        if pieza.getancho() <= tela.getlibre() and pieza.getalto() <= tela.getaltura() and pieza.getasignada() is False:
            tela.setusado(pieza.getancho())
            pieza.setasignada()
    #if pieza.getasignada() is False:
            telas.append(Tela(int(pieza.getalto()), ancho_del_telon))

#Finaliza constructivo

for pieza in piezas:
    print (pieza.tostring())


for tela in telas:
    print(tela.getlibre())
