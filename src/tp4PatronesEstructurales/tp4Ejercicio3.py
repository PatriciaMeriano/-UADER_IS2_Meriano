from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Pieza"

class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Subconjunto({'+'.join(results)})"

if __name__ == "__main__":
    # Crear el producto principal
    producto_principal = Composite()

    # Crear tres subconjuntos
    subconjunto1 = Composite()
    subconjunto2 = Composite()
    subconjunto3 = Composite()

    # Agregar cuatro piezas a cada subconjunto
    for _ in range(4):
        subconjunto1.add(Leaf())
        subconjunto2.add(Leaf())
        subconjunto3.add(Leaf())

    # Agregar los subconjuntos al producto principal
    producto_principal.add(subconjunto1)
    producto_principal.add(subconjunto2)
    producto_principal.add(subconjunto3)

    # Mostrar la estructura
    print(f"Producto Principal: {producto_principal.operation()}")

    # Agregar un subconjunto opcional
    subconjunto_opcional = Composite()
    for _ in range(4):
        subconjunto_opcional.add(Leaf())
    producto_principal.add(subconjunto_opcional)

    # Mostrar la estructura actualizada
    print(f"Producto Principal (con subconjunto opcional): {producto_principal.operation()}")
