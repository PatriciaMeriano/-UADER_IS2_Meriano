from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
   

    @abstractmethod
    def factory_method(self):
        
        pass

    def some_operation(self) -> str:
        

        # Call the factory method to create a Product object.
        hamburguesa = self.factory_method()

        # Now, use the product.
        result = hamburguesa.operation()
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> hamburguesa:
       return ConcreteProduct1()
       


class ConcreteCreator2(Creator):
    def factory_method(self) -> hamburguesa:
        return ConcreteProduct2()


class ConcreteCreator3(Creator):
    def factory_method(self) -> hamburguesa:
        return ConcreteProduct3()


class hamburguesa(ABC):
   

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(hamburguesa):
    def operation(self) -> str:
        return "{el producto se entrega en el mostrador}"


class ConcreteProduct2(hamburguesa):
    def operation(self) -> str:
        return "{el producto es retirado por el cliente}"

class ConcreteProduct3(hamburguesa):
    def operation(self) -> str:
        return "{el producto se envia con delivery}"
        
        
def client_code(creator: Creator) -> None:
   

    print(f"El producto se encuentra disponible para el cliente\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("Mostrador")
    client_code(ConcreteCreator1())
    print("\n")

    print("Cliente")
    client_code(ConcreteCreator2())
    print("\n")

    print("Delivery")
    client_code(ConcreteCreator3())