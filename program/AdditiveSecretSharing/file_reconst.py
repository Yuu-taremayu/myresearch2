def int_to_hex(DEC):
    re_HEX = ''
    for i in range(len(DEC)):
        h = str(format(DEC[i], 'x'))
        re_HEX += h

    with open('secret_reconst.hex', mode='w') as f:
        f.write(re_HEX)
