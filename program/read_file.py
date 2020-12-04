if __name__ == '__main__':
    HEX = ''
    with open('secret.hex') as s:
        for l in s:
            print(l, end='')
            #
            HEX += l
    print(HEX)
    print(HEX[0])

    DEC = []
    h = ''
    t = ''
    for i in range(len(HEX)):
        #print(HEX[i], end='')
        h = hex(int(HEX[i], 16))
        #print(h)
        t += h[2:]
        if i % 4 == 3:
            #print(int('0x'+t, 16))
            DEC.append(int('0x'+t, 16))
            t = ''
    print(DEC)
