def write_share(_name, _number, _shares):
    file_name = str(_name) + str(_number) + '.txt'
    with open(file_name, mode='w') as f:
        for i in range(len(_shares)):
            f.write(str(_shares[i])+'\n')
