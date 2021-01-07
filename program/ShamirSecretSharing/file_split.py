import sys

def hex_to_int():
    if len(sys.argv) < 2:
        print('too few arguments.')
        sys.exit()
    elif len(sys.argv) > 2:
        print('too many arguments.')
        sys.exit()

    file_name = sys.argv[1]
    HEX = ''
    with open(file_name, mode='r') as s:
        for l in s:
            HEX += l
    HEX = HEX.replace('\n', '')

    size = 4
    DEC = []
    h = ''
    temp = ''
    for i in range(len(HEX)):
        h = hex(int(HEX[i], 16))
        temp += h[2:]
        if i % size == size - 1:
            DEC.append(int('0x'+temp, 16))
            temp = ''

    return DEC
