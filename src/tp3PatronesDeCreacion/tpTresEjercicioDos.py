class Impuesto:
    def calcular(self, monto):
        raise NotImplementedError("Método calcular debe ser implementado por las subclases")

class ImpuestoIVA(Impuesto):
    def calcular(self, monto):
        return monto * 0.21

class ImpuestoIIBB(Impuesto):
    def calcular(self, monto):
        return monto * 0.05

class ImpuestoC_M(Impuesto):
    def calcular(self, monto):
        return monto * 0.012
    
class FabricaImpuestos:
    def crear_impuesto(self, tipo):
        if tipo == "IVA":
            return ImpuestoIVA()
        else:
            if tipo=="IIBB":
             return ImpuestoIIBB()
        
            else:
                if tipo == "C_M":
                     return ImpuestoC_M()
                else:
                  raise ValueError(f"Tipo de impuesto desconocido: {tipo}")

# Aplicando el Metodo Factory
fabrica = FabricaImpuestos()
impuesto_iva = fabrica.crear_impuesto("IVA")
impuesto_iibb = fabrica.crear_impuesto("IIBB")
impuesto_c_m= fabrica.crear_impuesto("C_M")

monto_factura = 195.000
print(f"Impuesto IVA (Valor Agregado): $ {impuesto_iva.calcular(monto_factura):.3f}")
print(f"Impuesto IIBB (Ingresos Brutos): $ {impuesto_iibb.calcular(monto_factura):.3f}")
print(f"Impuesto C_M (Contribuciones Municipales): $ {impuesto_c_m.calcular(monto_factura):.3f}")
