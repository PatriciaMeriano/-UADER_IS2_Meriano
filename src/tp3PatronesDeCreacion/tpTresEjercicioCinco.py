from abc import ABC, abstractmethod

# Clase Avión (Producto)
class Avion:
    def __init__(self):
        self.body = None
        self.turbinas = []
        self.alas = []
        self.tren_aterrizaje = None

    def especificaciones(self):
        print("Especificaciones del avión:")
        print(f"Tipo de cuerpo: {self.body}")
        print(f"Número de turbinas: {len(self.turbinas)}")
        print(f"Número de alas: {len(self.alas)}")
        print(f"Tren de aterrizaje: {self.tren_aterrizaje}")

# Interfaz Builder
class BuilderAvion(ABC):
    @abstractmethod
    def construir_body(self):
        pass

    @abstractmethod
    def construir_turbinas(self):
        pass

    @abstractmethod
    def construir_alas(self):
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self):
        pass

# ConcreteBuilder para Aviones Comerciales
class AvionComercialBuilder(BuilderAvion):
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.body = "Cuerpo comercial"

    def construir_turbinas(self):
        self.avion.turbinas = ["Turbofan 1", "Turbofan 2"]

    def construir_alas(self):
        self.avion.alas = ["Ala izquierda", "Ala derecha"]

    def construir_tren_aterrizaje(self):
        self.avion.tren_aterrizaje = "Tren comercial"

    def obtener_avion(self):
        return self.avion

# Director
class Director:
    def construir_avion(self, builder):
        builder.construir_body()
        builder.construir_turbinas()
        builder.construir_alas()
        builder.construir_tren_aterrizaje()
        return builder.obtener_avion()

# Ejemplo de uso
if __name__ == "__main__":
    director = Director()
    builder_comercial = AvionComercialBuilder()

    avion_comercial = director.construir_avion(builder_comercial)
    avion_comercial.especificaciones()

