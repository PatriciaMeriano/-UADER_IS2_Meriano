class Hamburguesa:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def entrega_en_mostrador(self):
        print(f"La hamburguesa '{self.nombre}' está lista para ser recogida en el mostrador.")

    def retira_cliente(self):
        print(f"El cliente ha retirado la hamburguesa '{self.nombre}'.")

    def envia_con_delivery(self):
        print(f"La hamburguesa '{self.nombre}' ha sido enviada por delivery.")

# Ejemplo de uso
if __name__ == "__main__":
    mi_hamburguesa = Hamburguesa (nombre = "Big MAc")
    mi_hamburguesa.entrega_en_mostrador()
    mi_hamburguesa.retira_cliente()
    mi_hamburguesa.envia_con_delivery()
