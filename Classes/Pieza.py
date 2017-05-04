class Pieza:
    def __init__(self, lado1, lado2, id):
        self.alto = min([lado1, lado2])
        self.ancho = max([lado1, lado2])
        self.id = id
        self.area = lado1 * lado2
        self.hilo = [self.id for x in range(int(self.ancho))]
        self.mapa = [self.hilo for x in range(int(self.alto))]
        self.asignada = False

    def tostring(self):
        return "Alto .- " + str(self.alto) + " Ancho .- " + str(self.ancho) + " ID: " + str(self.id) + " Area " + str(self.area) + " Asignada " + str(self.asignada)

    def getmap(self):
        return self.mapa

    def getalto(self):
        return self.alto

    def getancho(self):
        return self.ancho

    def getasignada(self):
        return self.asignada

    def setasignada(self):
        self.asignada = True

    def getid(self):
        return self.id
