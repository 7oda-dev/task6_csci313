def add(a, b):
    if not all(isinstance(i, (int, float)) for i in (a, b)):
        raise TypeError("Both arguments must be numbers.")
    return a + b
