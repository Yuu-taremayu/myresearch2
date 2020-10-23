import random

#
# generate server ids
#
def generate_server_id(n, p):
    server_id = [i + 1 for i in range(p - 1)]
    random.shuffle(server_id)
    print(f'elements of GF({p}) without 0 = {server_id}')
    for i in range(p - n):
        server_id.pop(0)
    print(f'server ids = {server_id}')
    return server_id

#
# generate coefficient of polynomial
#
def generate_polynomial(s, k, p):
    f_x = [s]
    for i in range(k - 1):
        f_x.append(random.randint(0, p - 1))
    print(f'f_x = {f_x}')
    return f_x

#
# create share
#
def create_share(server_id, f_x, p):
    w = []
    for i in server_id:
        share = 0
        for j in range(len(f_x)):
            share += f_x[j] * i ** j
        share %= p
        w.append(share)
    print(f'shares = {w}')
    return w

#
# calculation of Lagrange Interpolation
#
def lagrange_interpolation(dataX, dataY, p):
    data_num = len(dataX)
    x = 0
    l = 0
    L = 0
    for i in range(data_num):
        l1 = base_polynomial(data_num, i, x, dataX, p)
        l2 = base_polynomial(data_num, i, dataX[i], dataX, p)
        temp1, l2_inv, temp2 = xgcd(l2, p)
        l = l1 * l2_inv
        L += dataY[i] * l
    L %= p
    return L

def base_polynomial(data_num, i, x, dataX, p):
    l = 1
    for k in range(data_num):
        if i != k:
            l *= x - dataX[k]
    l = l % p
    return l

def xgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = xgcd(b % a, a)
        return g, x - (b // a) * y, y

def main():
    #
    # define some constant
    # s:secret k:key num n:share num p:prime
    #
    s = 12
    k = 4
    n = 11
    p = 31
    random.seed(0)

    print(f'GF({p})')
    #
    # split secret
    #
    server_id = generate_server_id(n, p)
    f_x = generate_polynomial(s, k, p)
    w = create_share(server_id, f_x, p)
    #
    # combine secret
    #
    L = lagrange_interpolation(server_id, w, p)

    print(f'L = {L}')
    if s == L:
        print('success!')
    else:
        print('failed...')

if __name__ == '__main__':
    main()
