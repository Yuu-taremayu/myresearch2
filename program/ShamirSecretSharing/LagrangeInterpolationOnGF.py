import random

def base_polynomial(data_num, i, x, dataX):
    l = 1
    for k in range(data_num):
        if i != k:
            l *= x - dataX[k]
    return l

def lagrange_interpolation(dataX, dataY):
    data_num = len(dataX)
    x = 0
    l = 0
    L = 0
    for i in range(data_num):
        l = base_polynomial(data_num, i, x, dataX) / base_polynomial(data_num, i, dataX[i], dataX)
        L += dataY[i] * l
    return L
