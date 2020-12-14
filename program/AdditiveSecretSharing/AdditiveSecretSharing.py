import random
import file_split as fsplit
import file_output as foutput
import file_read as fread
import file_reconst as freconst

#
# create share
#
def create_share(_secret, _n):
    share = []
    for i in range(1, _n):
        r = random.randint(-(2**63-1), 2**63-1)
        share.append(r)
    s = _secret - sum(share)
    share.insert(0, s)
    #print(f'share = {share}')
    return share

#
# combine share
#
def combine_share(_share):
    s = sum(_share)
    return s

def main():
    #
    # define some constant
    #
    secret = fsplit.hex_to_int()
    n = 10
    random.seed(0)

    #
    # disperse imformation
    #
    shares = []
    for i in range(len(secret)):
        shares.append(create_share(secret[i], n))

    #
    # write file
    #
    temp = []
    for i in range(len(shares[0])):
        for j in range(len(shares)):
            temp.append(shares[j][i])
        foutput.write_share('Share', i + 1, temp)
        temp = []

    #
    # read file
    #
    shares = fread.read_share('Share', n)

    #
    # reconstruct imformation
    #
    re_s = []
    for i in range(len(shares)):
        s = combine_share(shares[i])
        if secret[i] == s:
            print('success!')
            re_s.append(s)
        else:
            print('failed...')

    freconst.int_to_hex(re_s)

if __name__ == '__main__':
    main()
