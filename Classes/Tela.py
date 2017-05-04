class Tela:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        self.hilo = []
        self.hilo = [0 for x in range(self.anchura)]
        self.mapa = []
        self.mapa = [self.hilo for x in range(self.altura)]
        self.usado = 0

    def getmapa(self):
        return self.mapa

    def getlibre(self):
        return self.anchura - self.usado

    def setusado(self, por_usar):
        self.usado += por_usar

    def getaltura(self):
        return self.altura
