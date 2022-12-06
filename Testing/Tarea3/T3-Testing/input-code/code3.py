# Ejemplo 3

def sum_n(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            return n + sum_n(n-1)
    else:
        return None

sum_n(5)
sum_n(5)
sum_n(5)
sum_n(5)
