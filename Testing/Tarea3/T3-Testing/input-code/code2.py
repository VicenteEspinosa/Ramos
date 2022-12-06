# Ejemplo 2

def fibonacci(n):
    if 0 <= n < 2:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return None
    else:
        if n >= 2:
            return fibonacci(n-1) + fibonacci(n-2)
        else:
            return None

n = 7
fibonacci(7)
