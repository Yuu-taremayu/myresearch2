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
    for i in range(_prime -_n):
        serverId.pop(0)
    return serverId

#
# generate coefficient of polynomial
#
def generate_polynomial(_secret, _k, _prime):
    fx = [_secret]
    for i in range(_k - 1):
        fx.append(random.randint(0, _prime - 1))
    return fx

#
# create share
#
def create_share(_serverId, _fx, _prime):
    share = []
    for i in _serverId:
        temp = 0
        for j in range(len(_fx)):
            temp += _fx[j] * i ** j
        temp %= _prime
        share.append(temp)
    return share

#
# calculation of Lagrange Interpolation
#
def lagrange_interpolation(_dataX, _dataY, _prime):
    dataNum = len(_dataX)
    x = 0
    l = 0
    L = 0
    for i in range(dataNum):
        l1 = base_polynomial(dataNum, i, x, _dataX, _prime)
        l2 = base_polynomial(dataNum, i, _dataX[i], _dataX, _prime)
        temp1, l2_inv, temp2 = xgcd(l2, _prime)
        l = l1 * l2_inv
        L += _dataY[i] * l
    L %= _prime
    return L

#
# calculation of base polynomial for Lagrange Interpolation
#
def base_polynomial(_dataNum, _i, _x, _dataX, _prime):
    l = 1
    for k in range(_dataNum):
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
# choose share randomly by the number of share_num and make list
#
def choose_share(serverId, w, n, share_num):
    use_share = [i for i in range(n - 1)]
    random.shuffle(use_share)
    for i in range(n - share_num):
        use_share.pop(0)
    print(f'using share number = {use_share}')
    dataX = []
    dataY = []
    for i in use_share:
        dataX.append(serverId[i - 1])
        dataY.append(w[i - 1])
    return dataX, dataY

def main():
    #
    # define some constant
    # secret:original secret  k:key num  n:share num  prime:prime
    #
    secret = fsplit.hex_to_int()
    k = 4
    n = 11
    prime = 65537
    random.seed(0)

    #
    # split secret
    # generate server id and n degree polynomial then calculate share
    #
    fx = []
    shares = []
    serverId = generate_serverId(n + 1, prime)
    for i in range(len(secret)):
        fx = generate_polynomial(secret[i], k, prime)
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
    shares = fread.read_share('Share', k+1)
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
        s = lagrange_interpolation(dataX, dataY[i], prime)
        if secret[i] == s:
            re_s.append(s)
        else:
            freconst.int_to_hex(re_s)

if __name__ == '__main__':
    main()
