dict = {0: 1, 1: 2}

def num_no(num):
    if num not in dict:
        dict[num] = num_no(num - 1) + num_no(num - 2)
    return dict[num]

def num_yes(num):
    tempele = num_no(num)
    return pow(2, num) - tempele