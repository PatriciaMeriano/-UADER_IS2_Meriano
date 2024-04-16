class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Calculo_Factorial(metaclass=SingletonMeta):
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
        
        
    
        

# Ejemplo de uso:
calculo_factorial = Calculo_Factorial()

num = 15
print(f"El factorial de {num} es: {calculo_factorial.factorial(num)}")

# Otro ejemplo de uso en otro lugar del código
otro_calculo_factorial = Calculo_Factorial()
print(f"El factorial de 10 es: {otro_calculo_factorial.factorial(10)}")



if __name__ == "__main__":
    # The client code.

    f1 = Calculo_Factorial()
    f2 = Calculo_Factorial()

    if id(f1) == id(f2):
        print("Singleton funciona bien, ambas variables contienen la misma instancia.")
    else:
        print("Singleton falla, ambas variables contienen instancias diferentes.")
