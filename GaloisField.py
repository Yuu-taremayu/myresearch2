def add(a, b, p):
    return (a + b) % p

def sub(a, b, p):
    if a - b >= 0:
        return (a - b) % p
    else:
        return (a - b + p) % p

def mul(a, b, p):
    return (a * b) % p

def div(a, b, p):
    g, x, y = EGCD(p, b)

    if (x < 0):
        i = 1
        while (a + i * p) % p < 0:
            i += 1
        x = (a + i * p) % p

    return (a * x) % p

def EGCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = EGCD(b % a, a)
        return g, x - (b // a) * y, y
