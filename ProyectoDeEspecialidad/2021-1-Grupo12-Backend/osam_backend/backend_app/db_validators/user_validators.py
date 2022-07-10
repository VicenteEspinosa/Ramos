from itertools import cycle


def validate_rut(rut):
    """Validate if the rut is correct."""

    try:
        run, digit_run = rut.split("-")
        reversed_digits = map(int, reversed(run))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        digit = (-s) % 11
    except ValueError:
        return False

    # Validate the minimun length
    if not ((len(run) == 7) or (len(run) == 8)):
        return False
    
    # Validate the verifier digit
    if (digit == 10) and ("k" == digit_run.lower()):
        return True
    if (digit != 10) and (str(digit) == digit_run):
        return True
    
    # If the RUT is wrong
    return False
