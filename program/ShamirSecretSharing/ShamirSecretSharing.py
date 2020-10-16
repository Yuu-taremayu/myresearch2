from GaloisField import GF
import random

#
# generate server ids
#
def generate_server_id(n, p):
    server_id = [i + 1 for i in range(p - 1)]
    random.shuffle(server_id)
    print(server_id)
    for i in range(p - n):
        server_id.pop(0)
    print(server_id)
    return server_id

#
# generate coefficient of polynomial
#
def generate_polynomial(s, k, p):
    f_x = [s]
    for i in range(k - 1):
        f_x.append(random.randint(0, p - 1))
    print(f'f_x = {f_x}')
    return f_x

#
# create share
#
def create_share(server_id, f_x):
    w = []
    for i in server_id:
        share = 0
        for j in range(len(f_x)):
            share += f_x[j] * i ** j
        w.append(share)
        print(f'share = {share}')

    return w

def main():
    #
    # define some constant
    # s:secret k:key num n:share num p:prime
    #
    s = 1
    k = 2
    n = 3
    p = 5
    random.seed(0)

    server_id = generate_server_id(n, p)
    f_x = generate_polynomial(s, k, p)
    w = create_share(server_id, f_x)

if __name__ == '__main__':
    main()
