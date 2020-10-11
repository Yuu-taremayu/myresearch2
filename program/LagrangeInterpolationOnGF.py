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
    dataX = [0.0, 1.0]
    dataY = [0.0, 3.0]
    data_num = len(dataX)
    x = 122.0
    y = lagrange_interpolation(data_num, x, dataX, dataY)
    print(y)
    '''
    GF.space = 11
    dataX = range(2)
    rand = [random.randint(0, 10) for i in range(2)]
    dataY = []
    for i in range(len(rand)):
        dataY.append(GF(rand[i]))
    data_num = len(dataX)
    for i in range(2):
        print(f'x[{i}] = {dataX[i]}, y[{i}] = {dataY[i].value}')
    x = GF(12)
    y = lagrange_interpolation(data_num, x.value, dataX, dataY)
    print(y)

    for i in range(len(dataX)):
        plt.scatter(dataX[i], dataY[i].value, label='dataset')
    plt.scatter(x.value, y, label='interpolation')
    plt.show()
    '''

if __name__ == '__main__':
    main()
