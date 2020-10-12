class GF():
    def __init__(self, x):
        self.value = x
    
    #
    # set modulo number
    #
    space = 5
    def set_space(num):
        GF.space = num

    #
    # overload of operands
    #
    def __add__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.add(self.value, y.value, GF.space))

    def __sub__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.sub(self.value, y.value, GF.space))

    def __mul__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.mul(self.value, y.value, GF.space))

    def __truediv__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.mul(self.value, y.value, GF.space))

    def __radd__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.add(self.value, y.value, GF.space))

    def __rsub__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.sub(self.value, y.value, GF.space))

    def __rmul__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.mul(self.value, y.value, GF.space))

    def __rtruediv__(self, y):
        if type(y) is int:
            y = GF(y)
        return (GF.mul(self.value, y.value, GF.space))

    #
    # calculation
    #
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
