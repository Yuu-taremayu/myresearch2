def read_share(_n):
    shares = []
    for i in range(_n):
        temp = []
        filename = 'Share' + str(i + 1) + '.txt'
        with open(filename, mode='r') as f:
            for l in f:
                l = l[:-1]
                temp.append(int(l))
        shares.append(temp)
    shares = [[shares[i][j] for i in range(len(shares))] for j in range(len(shares[0]))]
    return shares
