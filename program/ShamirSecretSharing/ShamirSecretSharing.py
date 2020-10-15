from GaloisField import GF
import random

def main():
    #
    # define some constant
    #
    s = 1
    k = 2
    n = 3
    p = 5
    GF.space = p
    random.seed(0)
    
    #
    # generate server ids
    #
    server_id = [random.randint(0, p - 1) for i in range(n)]
    while len(server_id) != len(set(server_id)):
        server_id = [random.randint(0, p - 1) for i in range(n)]
    print(f'server_id = {server_id}')

    #
    # generate coefficient of polynomial
    #
    f_x = [s]
    for i in range(k - 1):
        f_x.append(random.randint(0, p - 1))
    print(f'f_x = {f_x}'

if __name__ == '__main__':
    main()
