import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcula el número de Collatz para los números del 1 al 10000
collatz_numbers = [collatz(i) for i in range(1, 10001)]

# Grafica el número de iteraciones vs el número inicial de la secuencia
plt.figure(figsize=(10, 6))
plt.scatter(range(1, 10001), collatz_numbers, marker='o', s=5)
plt.title('Conjetura de Collatz (Iteraciones vs Número inicial)')
plt.xlabel('Número inicial de la secuencia')
plt.ylabel('Número de iteraciones para converger')
plt.grid(True)
plt.show()
