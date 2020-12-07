import random

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
    print(f'share = {share}')
    return share

def combine_share(_share):
    s = sum(_share)
    return s

def main():
    #
    # define some constant
    #
    secret = 13
    n = 10
    random.seed(0)

    #
    # disperse imformation
    #
    share = create_share(secret, n)

    #
    # reconstruct imformation
    #
    s = combine_share(share)

    if secret == s:
        print('success!')
    else:
        print('failed...')

if __name__ == '__main__':
    main()
