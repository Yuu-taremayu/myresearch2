import random

#
# generate server ids
#
def generate_server_id(n, prime):
    server_id = [i + 1 for i in range(prime - 1)]
    random.shuffle(server_id)
    print(f'shuffled elements of GF({prime}) without 0 = {server_id}')
    for i in range(prime - n):
        server_id.pop(0)
    print(f'server ids = {server_id}')
    return server_id

#
# generate coefficient of polynomial
#
def generate_polynomial(secret, k, prime):
    f_x = [secret]
    for i in range(k - 1):
        f_x.append(random.randint(0, prime - 1))
    print(f'f_x = {f_x}')
    return f_x

#
# create share
#
def create_share(server_id, f_x, prime):
    share = []
    for i in server_id:
        temp = 0
        for j in range(len(f_x)):
            temp += f_x[j] * i ** j
        temp %= prime
        share.append(temp)
    print(f'shares = {share}')
    return share

#
# calculation of Lagrange Interpolation
#
def lagrange_interpolation(dataX, dataY, prime):
    data_num = len(dataX)
    x = 0
    l = 0
    L = 0
    for i in range(data_num):
        l1 = base_polynomial(data_num, i, x, dataX, prime)
        l2 = base_polynomial(data_num, i, dataX[i], dataX, prime)
        temp1, l2_inv, temp2 = xgcd(l2, prime)
        l = l1 * l2_inv
        L += dataY[i] * l
    L %= prime
    return L

def base_polynomial(data_num, i, x, dataX, prime):
    l = 1
    for k in range(data_num):
        if i != k:
            l *= x - dataX[k]
    l = l % prime
    return l

def xgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = xgcd(b % a, a)
        return g, x - (b // a) * y, y

def choose_share(server_id, w, n, share_num):
    use_share = [i for i in range(n - 1)]
    random.shuffle(use_share)
    for i in range(n - share_num):
        use_share.pop(0)
    print(f'using share number = {use_share}')
    dataX = []
    dataY = []
    for i in use_share:
        dataX.append(server_id[i - 1])
        dataY.append(w[i - 1])
        print(i)
    print(dataX)
    return dataX, dataY

def main():
    #
    # define some constant
    # ssecret:original secret  k:key num  n:share num  prime:prime
    #
    secret = 12
    k = 4
    n = 11
    prime = 31
    random.seed(0)

    print(f'GF({prime})')

    #
    # split secret
    #
    server_id = generate_server_id(n, prime)
    f_x = generate_polynomial(secret, k, prime)
    share = create_share(server_id, f_x, prime)

    #
    # combine secret
    #
    share_num = 1
    dataX, dataY = choose_share(server_id, share, n, share_num)
    L = lagrange_interpolation(dataX, dataY, prime)

    print(f'L = {L}')
    if secret == L:
        print('success!')
    else:
        print('failed...')

if __name__ == '__main__':
    main()
