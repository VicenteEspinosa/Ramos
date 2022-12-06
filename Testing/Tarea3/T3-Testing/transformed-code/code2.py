def fibonacci(n):
    Profile.record('fibonacci', [n])
    if 0 <= n < 2:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return None
    elif n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return None
n = 7