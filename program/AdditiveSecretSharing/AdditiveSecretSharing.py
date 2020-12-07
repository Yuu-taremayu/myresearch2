import random
import file_split as fs
import file_output as fo

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
    secret = fs.file_to_int()
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
        fo.write_share(i + 1, temp)
        temp = []

    #
    # reconstruct imformation
    #
    for i in range(len(shares)):
        s = combine_share(shares[i])
        '''
        if secret[i] == s:
            print('success!')
        else:
            print('failed...')
        '''

if __name__ == '__main__':
    main()
