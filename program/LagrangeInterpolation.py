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
        L += dataY[i] * l
    return L

def main():
    dataX = [0.0, 1.0]
    dataY = [0.0, 3.0]
    data_num = len(dataX)
    x = 122.0
    y = lagrange_interpolation(data_num, x, dataX, dataY)
    print(y)

if __name__ == '__main__':
    main()
