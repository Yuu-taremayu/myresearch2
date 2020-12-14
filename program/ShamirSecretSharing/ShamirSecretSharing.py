import random
import file_split as fsplit
import file_output as foutput
import file_read as fread
import file_reconst as freconst

#
# generate server ids
#
def generate_server_id(_n, _prime):
    server_id = [i + 1 for i in range(_prime - 1)]
    random.shuffle(server_id)
    #print(f'shuffled elements of GF({_prime}) without 0 = {server_id}')
    for i in range(_prime -_n):
        server_id.pop(0)
    print(f'server ids = {server_id}')
    return server_id

#
# generate coefficient of polynomial
#
def generate_polynomial(_secret, _k, _prime):
    f_x = [_secret]
    for i in range(_k - 1):
        f_x.append(random.randint(0, _prime - 1))
    #print(f'f_x = {f_x}')
    return f_x

#
# create share
#
def create_share(_server_id, _f_x, _prime):
    share = []
    for i in _server_id:
        temp = 0
        for j in range(len(_f_x)):
            temp += _f_x[j] * i ** j
        temp %= _prime
        share.append(temp)
    #print(f'shares = {share}')
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
def base_polynomial(data_num, i, x, dataX, prime):
    l = 1
    for k in range(data_num):
        if i != k:
            l *= x - dataX[k]
    l = l % prime
    return l

#
# calculation of inverse element on Galois Field
#
def xgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = xgcd(b % a, a)
        return g, x - (b // a) * y, y

#
# choose share randomly by the number of share_num and make list
#
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
    return dataX, dataY

def main():
    #
    # define some constant
    # secret:original secret  k:key num  n:share num  prime:prime
    #
    #secret = 12
    secret = fsplit.hex_to_int()
    k = 4
    n = 11
    prime = 65537
    random.seed(0)

    #print(f'GF({prime})')

    #
    # split secret
    # generate server id and n degree polynomial then calculate share
    #
    '''
    server_id = generate_server_id(n + 1, prime)
    f_x = generate_polynomial(secret, k, prime)
    shares = create_share(server_id, f_x, prime)
    '''

    f_x = []
    shares = []
    server_id = generate_server_id(n + 1, prime)
    for i in range(len(secret)):
        f_x = generate_polynomial(secret[i], k, prime)
        shares.append(create_share(server_id, f_x, prime))
    #print(shares)

    for i in range(len(shares[0])):
        temp = [server_id[i]]
        for j in range(len(shares)):
            temp.append(shares[j][i])
        foutput.write_share('Share', i + 1, temp)
    
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
    # choose share and combine secret
    # share_num:the number of share for interpolation
    #
    '''
    share_num = 10
    dataX, dataY = choose_share(server_id, shares[i], n + 1, share_num + 1)
    L = lagrange_interpolation(dataX, dataY, prime)
    print(f'L = {L}')
    if secret[i] == L:
        print('success!')
    else:
        print('failed...')
    '''

    re_s = []
    for i in range(len(dataY)):
        L = lagrange_interpolation(dataX, dataY[i], prime)
        print(f'L = {L}')
        if secret[i] == L:
            print('success!')
            re_s.append(L)
        else:
            print('failed...')

    freconst.int_to_hex(re_s)

if __name__ == '__main__':
    main()
