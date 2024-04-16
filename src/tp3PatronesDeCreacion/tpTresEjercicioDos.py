class CalculadoraImpuestos:
    def __init__(self, base_imponible):
        self.base_imponible = base_imponible

    def calcular_iva(self):
        iva = self.base_imponible * 0.21
        return iva

    def calcular_iibb(self):
        iibb = self.base_imponible * 0.05
        return iibb

    def calcular_contribuciones_municipales(self):
        contribuciones = self.base_imponible * 0.012
        return contribuciones

    

# Ejemplo de uso:
importe_base = 1000  # Reemplaza con el valor de importe base imponible que desees
calculadora = CalculadoraImpuestos(importe_base)

iva = calculadora.calcular_iva()
iibb = calculadora.calcular_iibb()
contribuciones = calculadora.calcular_contribuciones_municipales()

print(f"el importe base es: ${importe_base:.2f}")
print(f"Importe a pagar de iva: ${iva:.2f}")
print(f"Importe a pagar de iibb: ${iibb:.2f}")
print(f"Importe a pagar de contribuciones municipales: ${contribuciones:.2f}")
