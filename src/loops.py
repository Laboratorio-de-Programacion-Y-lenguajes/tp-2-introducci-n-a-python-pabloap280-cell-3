# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    for i in range(1, n + 1):
        return list(range(1, n + 1))
    pass


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    for i in range(1, 11):
        return [n * i for i in range(1, 11)]
    pass


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    suma = 0
    for digito in str(n):   
        suma += int(digito)
    return suma
    pass


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    pass


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibo = [0, 1]
        for i in range(2, n):
            siguiente = fibo[i - 1] + fibo[i - 2]
            fibo.append(siguiente)
        return fibo
    pass
