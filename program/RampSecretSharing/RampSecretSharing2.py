import random
from sympy import Matrix
import file_split as fsplit
import file_output as foutput
import file_read as fread
import file_reconst as freconst

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
    if bitLen%8 != 0:
        secBit = format(_secret, '0' + str(bitLen + (8 - bitLen%8)) + 'b')
        bitLen = len(secBit)
    fx = []
    for i in range(_L):
        temp = secBit[i*int(bitLen/_L):(i+1)*int(bitLen/_L)]
        fx.append(int(temp, 2))
    for i in range(_L, _k-1):
        fx.append(random.randint(0, _prime-1))
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

#
# reconstruct secrets
#
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

    bit = ''
    for i in range(_L):
        temp = format(int(ansMat[i]), 'b')
        if len(temp)%8 != 0:
            temp = format(int(ansMat[i]), '0' + str(len(temp) + (8 - len(temp)%8)) + 'b')
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
    secret = fsplit.hex_to_int()
    k = 4
    L = 2
    n = 11
    prime = 65537
    random.seed(0)

    #
    # split secret
    # generate server id and n degree polynomial then calculate share
    #
    fx = []
    shares = []
    serverId = generate_serverId(n+1, prime)
    for i in range(len(secret)):
        fx = generate_polynomial(secret[i], k, L, prime)
        shares.append(create_share(serverId, fx, prime))

    #
    # write file
    #
    for i in range(len(shares[0])):
        temp = [serverId[i]]
        for j in range(len(shares)):
            temp.append(shares[j][i])
        foutput.write_share('Share', i + 1, temp)

    #
    # read file
    #
    shares = fread.read_share('Share', k + 1)
    dataX = []
    dataY = []
    for i in range(len(shares[0])):
        dataX.append(shares[0][i])
    for i in range(1, len(shares)):
        temp = []
        for j in range(len(shares[0])):
            temp.append(shares[i][j])
        dataY.append(temp)
    
    #
    # reconstruct information
    #
    re_s = []
    for i in range(len(dataY)):
        s = reconst_secret(dataX, dataY[i], prime, k, L)
        if secret[i] == s:
            re_s.append(s)
    freconst.int_to_hex(re_s)

if __name__ == '__main__':
    main()
