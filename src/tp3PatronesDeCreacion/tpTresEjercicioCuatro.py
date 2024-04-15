class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def generar_factura(self):
        print(f"Factura generada por un importe total de: ${self.importe: .2f}")
        print(f"Condición impositiva: {self.condicion_impositiva}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una factura con diferentes condiciones impositivas
    factura1 = Factura(importe=50000, condicion_impositiva="IVA Responsable")
    factura2 = Factura(importe=1500, condicion_impositiva="IVA No Inscripto")
    factura3 = Factura(importe=30000, condicion_impositiva="IVA Exento")

    # Generar las facturas
    factura1.generar_factura()
    factura2.generar_factura()
    factura3.generar_factura()
