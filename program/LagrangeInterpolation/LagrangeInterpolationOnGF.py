from GaloisField import GF
import random
import matplotlib.pyplot as plt

def base_polynomial(data_num, i, x, dataX):
    l = 1
    for k in range(data_num):
        if i != k:
            l *= x - dataX[k]
    return l

def lagrange_interpolation(data_num, x, dataX, dataY):
    l = 0
    L = 0
    for i in range(data_num):
        l = base_polynomial(data_num, i, x, dataX) / base_polynomial(data_num, i, dataX[i], dataX)
        L += dataY[i] * int(l)
    return L

def main():
    dataX = []
    dataY = []
    random.seed(0)
    dataX = [GF(i) for i in range(3)]
    dataY = [GF(random.randint(0, 10)) for i in range(3)]
    for i in range(3):
        print(f'(x_{i}, y_{i}) = ({dataX[i].value}, {dataY[i].value})')
    data_num = len(dataX)
    GF.space = 5
    x = GF(122.0)
    y = lagrange_interpolation(data_num, x, dataX, dataY)
    print(f'x_orig = {x.value}')
    print(f'y value = {y}')

if __name__ == '__main__':
    main()
