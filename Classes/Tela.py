class Tela:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        self.hilo = []
        self.hilo = [0 for x in range(self.anchura)]
        self.mapa = []
        self.mapa = [self.hilo for x in range(self.altura)]
        self.usado = 0
        self.cosido = []

    def getmapa(self):
        return self.mapa

    def getlibre(self):
        return self.anchura - self.usado

    def setusado(self, por_usar):
        self.usado += por_usar

    def getaltura(self):
        return self.altura

    def tostring(self):
        return "Altura: " + str(self.altura) + " Usado: " + str(self.usado) + " Asignados " + str(self.cosido)

    def coser(self, pieza_id):
        self.cosido.append(pieza_id)

    def getcosidos(self):
        return self.cosido
