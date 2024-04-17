from abc import ABC, abstractmethod

# Interfaz abstracta para representar las láminas de acero
class Lamina(ABC):
    @abstractmethod
    def producir(self):
        pass

# Clase concreta para láminas de 5 metros
class Lamina5Metros(Lamina):
    def producir(self):
        print("Produciendo lámina de 5 metros")

# Clase concreta para láminas de 10 metros
class Lamina10Metros(Lamina):
    def producir(self):
        print("Produciendo lámina de 10 metros")

# Clase de implementación para los trenes laminadores
class TrenLaminador:
    def producir_lamina(self, lamina: Lamina):
        lamina.producir()

# Clase abstracción que conecta láminas y trenes laminadores
class LaminaBridge:
    def __init__(self, lamina: Lamina, tren_laminador: TrenLaminador):
        self.lamina = lamina
        self.tren_laminador = tren_laminador

    def producir(self):
        self.tren_laminador.producir_lamina(self.lamina)

# Ejemplo de uso
if __name__ == "__main__":
    lamina_5m = Lamina5Metros()
    lamina_10m = Lamina10Metros()

    tren_laminador_5m = TrenLaminador()
    tren_laminador_10m = TrenLaminador()

    lamina_bridge_5m = LaminaBridge(lamina_5m, tren_laminador_5m)
    lamina_bridge_10m = LaminaBridge(lamina_10m, tren_laminador_10m)

    lamina_bridge_5m.producir()  # Produciendo lámina de 5 metros
    lamina_bridge_10m.producir()  # Produciendo lámina de 10 metros
