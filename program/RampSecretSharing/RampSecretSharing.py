import random
from sympy import Matrix

#
# generate server ids
#
def generate_serverId(_n, _prime):
    serverId = [i+1 for i in range(_prime-1)]
    random.shuffle(serverId)
    for i in range(_prime-_n):
        serverId.pop(0)
    return serverId

#
# generate coefficient of polynomial
#
def generate_polynomial(_secret, _k, _L, _prime):
    secBit = format(_secret, 'b')
    bitLen = len(secBit)
    if bitLen%4 != 0:
        secBit = format(_secret, '0' + str(bitLen + (4 - bitLen%4)) + 'b')
        bitLen = len(secBit)
    fx = []
    for i in range(_L):
        temp = secBit[i*int(bitLen/_L):(i+1)*int(bitLen/_L)]
        print(temp)
        fx.append(int(temp, 2))
    for i in range(_L, _k-1):
        fx.append(random.randint(0, _prime-1))
    print('f(x) =', fx)
    return fx

#
# create share
#
def create_share(_serverId, _fx, _prime):
    share = []
    for i in _serverId:
        temp = 0
        for j in range(len(_fx)):
            temp += _fx[j] * i**j
        temp %= _prime
        share.append(temp)
    return share

def reconst_secret(_dataX, _dataY, _prime, _k, _L):
    num = len(_dataX)
    xList = []
    for x in _dataX:
        for i in range(num):
            xList.append((x ** i) % _prime)
    xMat = Matrix(num, num, xList)
    yMat = Matrix(num, 1, _dataY)
    xMat = xMat.inv_mod(_prime)
    ansMat = (xMat * yMat) % _prime
    print(ansMat)

    bit = ''
    for i in range(_L):
        temp = format(int(ansMat[i]), 'b')
        bit += temp
    secret = int(bit, 2)
    return secret

#
# choose share randomly by the number of shareNum and make list
#
def choose_share(_serverId, _w, _n, _shareNum):
    useShare = [i for i in range(_n-1)]
    random.shuffle(useShare)
    for i in range(_n-_shareNum):
        useShare.pop(0)
    dataX = []
    dataY = []
    for i in useShare:
        dataX.append(_serverId[i-1])
        dataY.append(_w[i-1])
    return dataX, dataY

def main():
    #
    # define some constant
    # secret:original secret  k:key num  n:share num  prime:prime
    #
    secret = 255
    k = 4
    L = 2
    n = 11
    prime = 65537
    random.seed(0)

    #
    # split secret
    # generate server id and n degree polynomial then calculate share
    #
    serverId = generate_serverId(n+1, prime)
    fx = generate_polynomial(secret, k, L, prime)
    shares = create_share(serverId, fx, prime)

    #
    # choose share and combine secret
    # shareNum:the number of share for interpolation
    #
    shareNum = 10
    dataX, dataY = choose_share(serverId, shares, n+1, shareNum+1)
    s = reconst_secret(dataX, dataY, prime, k, L)

    if secret == s:
        print('success!')
    else:
        print('failed...')

if __name__ == '__main__':
    main()
