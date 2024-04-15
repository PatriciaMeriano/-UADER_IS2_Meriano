class CalculoFactorial:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

# Ejemplo de uso:
calculo_factorial = CalculoFactorial()

num = 10
print(f"El factorial de {num} es: {calculo_factorial.factorial(num)}")

# Otro ejemplo de uso en otro lugar del código
otro_calculo_factorial = CalculoFactorial()
print(f"El factorial de 3 es: {otro_calculo_factorial.factorial(3)}")

# Verificar si son la misma instancia
print(calculo_factorial is otro_calculo_factorial)  # Debería imprimir True
