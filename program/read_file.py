if __name__ == '__main__':
    HEX = ''
    with open('secret.hex') as s:
        for l in s:
            print(l, end='')
            #
            HEX += l
    print(HEX)
    print(HEX[0])

    for i in range(len(HEX)):
        print(HEX[i], end='')
        if i % 4 == 3:
            print()
