def EGCD(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = EGCD(b % a, a)
        return g, x - (b // a) * y, y
