import copy
import time

#creamos una clase de prototipo generico
class Prototipo:
    def clone(self):
        return copy.deepcopy(self)

#clase que hereda de prototipo
class ObjetoHijo(Prototipo):
    def __init__(self, name):
        self.name = name

    def process(self):
        # Simula el proceso con un tiempo de 2 segundos
        time.sleep(2)
        print(f"Procesando {self.name}")

if __name__ == "__main__":
    # Crea un prototipo inicial
    prototipo_base= ObjetoHijo("Patron Prototype")

    # Generar 20 anidamientos
    anidamiento_prototype = prototipo_base
    for i in range(20):
        anidamiento_prototype = anidamiento_prototype.clone()
        anidamiento_prototype.process()
