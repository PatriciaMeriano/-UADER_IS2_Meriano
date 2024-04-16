from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
   

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        # Call the factory method to create a Factura object.
        factura = self.factory_method()

        # Now, use the product.
        result = f"{factura.operation()}\n"

        return result


class ConcreteCreator1(Creator):
  
    def factory_method(self) -> Product:
        return ConcreteFactura1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteFactura2()
    
        
class ConcreteCreator3(Creator):
    def factory_method(self) -> Product:
        return ConcreteFactura3()


class Product(ABC):
   

    @abstractmethod
    def operation(self) -> str:
        pass
    
    


class ConcreteFactura1(Product):
    def operation(self) -> str:
        return "Declarado Responsable Inscripto ante IVA"


class ConcreteFactura2(Product):
    def operation(self) -> str:
        return "Declarado No Inscripto ante IVA"
    
class ConcreteFactura3(Product):
    def operation(self) -> str:
        return "Declarado Excento ante IVA"

def client_code(creator: Creator) -> None:
   

    print(f"Se esta creando una Factura correspondiente a: \n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("Responsable_Inscripto")
    client_code(ConcreteCreator1())
    print("\n")

    print("Responsable No Inscripto")
    client_code(ConcreteCreator2())
    print("\n")

    print("Excento")
    client_code(ConcreteCreator3())
