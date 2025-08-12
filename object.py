class Dron:
    def __init__(self, modelo, alturaMax, bateria, camara="sin cámara"):
        self.__modelo = modelo
        self.__alturaMax = alturaMax
        self.__bateria = bateria
        self.__camara = camara
        self.__distanciaTotal = 0
  
    def volar(self, distancia):
        consumo = distancia // 100  # gasta 1% por cada 100m

        if self.__bateria <= 0:
            return "El Dron no puede volar porque no tiene bateria."

        if consumo == 0 and distancia > 0:
            consumo = 1  # Al menos 1% por intento de vuelo

        if consumo > self.__bateria:
            return "El Dron no tiene suficiente batería para esa distancia."

        self.__bateria -= consumo
        self.__distanciaTotal += distancia
        return f"El dron voló {distancia} metros. Batería restante: {self.__bateria}%"

    def cargarBateria(self, cantidad):
        self.__bateria += cantidad
        if self.__bateria >= 100:
            self.__bateria = 100
        return f"Batería cargada. Bateria actual: {self.__bateria}%"

    def activarCamara(self):
        if self.__camara == "sin cámara":
            return "Este dron no tiene cámara."
        else:
            return "Cámara activada y grabando."

    def __str__(self):
        return (
            f"Modelo: {self.__modelo}\n"
            f"AlturaMax: {self.__alturaMax} m\n"
            f"Batería: {self.__bateria}%\n"
            f"Cámara: {self.__camara}\n"
            f"Distancia total que voló: {self.__distanciaTotal} metros"
        )

         