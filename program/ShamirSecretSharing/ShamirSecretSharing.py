import random
import file_split as fsplit
import file_output as foutput
import file_read as fread
import file_reconst as freconst

#
# generate server ids
#
def generate_serverId(_n, _prime):
    serverId = [i + 1 for i in range(_prime - 1)]
    random.shuffle(serverId)
    print(f'shuffled elements of GF({_prime}) without 0 = {serverId}')
    for i in range(_prime -_n):
        serverId.pop(0)
    print(f'server ids = {serverId}')
    return serverId

#
# generate coefficient of polynomial
#
def generate_polynomial(_secret, _k, _prime):
    f_x = [_secret]
    for i in range(_k - 1):
        f_x.append(random.randint(0, _prime - 1))
    print(f'f_x = {f_x}')
    return f_x

#
# create share
#
def create_share(_serverId, _f_x, _prime):
    share = []
    for i in _serverId:
        temp = 0
        for j in range(len(_f_x)):
            temp += _f_x[j] * i ** j
        temp %= _prime
        share.append(temp)
    print(f'shares = {share}')
    return share

#
# calculation of Lagrange Interpolation
#
def lagrange_interpolation(_dataX, _dataY, _prime):
    data_num = len(_dataX)
    x = 0
    l = 0
    L = 0
    for i in range(data_num):
        l1 = base_polynomial(data_num, i, x, _dataX, _prime)
        l2 = base_polynomial(data_num, i, _dataX[i], _dataX, _prime)
        temp1, l2_inv, temp2 = xgcd(l2, _prime)
        l = l1 * l2_inv
        L += _dataY[i] * l
    L %= _prime
    return L

#
# calculation of base polynomial for Lagrange Interpolation
#
def base_polynomial(_data_num, _i, _x, _dataX, _prime):
    l = 1
    for k in range(_data_num):
        if _i != k:
            l *= _x - _dataX[k]
    l = l % _prime
    return l

#
# calculation of inverse element on Galois Field
#
def xgcd(_a, _b):
    if _a == 0:
        return _b, 0, 1
    else:
        g, y, x = xgcd(_b%_a, _a)
        return g, x - (_b//_a)*y, y

#
# choose share randomly by the number of shareNum and make list
#
def choose_share(_serverId, _w, _n, _shareNum):
    use_share = [i for i in range(_n - 1)]
    random.shuffle(use_share)
    for i in range(_n - _shareNum):
        use_share.pop(0)
    print(f'using share number = {use_share}')
    dataX = []
    dataY = []
    for i in use_share:
        dataX.append(_serverId[i - 1])
        dataY.append(_w[i - 1])
    return dataX, dataY

def main():
    #
    # define some constant
    # secret:original secret  k:key num  n:share num  prime:prime
    #
    secret = 12
    k = 4
    n = 11
    prime = 65537
    random.seed(0)

    print(f'GF({prime})')

    #
    # split secret
    # generate server id and n degree polynomial then calculate share
    #
    serverId = generate_serverId(n + 1, prime)
    f_x = generate_polynomial(secret, k, prime)
    shares = create_share(serverId, f_x, prime)

    #
    # choose share and combine secret
    # shareNum:the number of share for interpolation
    #
    shareNum = 10
    dataX, dataY = choose_share(serverId, shares, n + 1, shareNum + 1)
    s = lagrange_interpolation(dataX, dataY, prime)
    print(f'reconstruct secret = {s}')
    if secret == s:
        print('success!')
    else:
        print('failed...')

if __name__ == '__main__':
    main()
