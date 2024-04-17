class Component:
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

class OperacionesNumericas:
    def __init__(self, numero):
        self.numero = numero

    def sumar(self, valor):
        self.numero += valor
        return self

    def multiplicar(self, valor):
        self.numero *= valor
        return self

    def dividir(self, valor):
        if valor != 0:
            self.numero /= valor
        return self

    def mostrar_resultado(self):
        print(f"Resultado: {self.numero}")

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Cliente: Tengo un componente simple:\n")
    client_code(simple)
    
    print("\n")
    
    numero_inicial = float(input("Ingrese un número: "))
    operaciones = OperacionesNumericas(numero_inicial)
    operaciones.sumar(2).multiplicar(2).dividir(3).mostrar_resultado()
    
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Cliente: Ahora tengo un componente decorado:")
    client_code(decorator2)




 

   
