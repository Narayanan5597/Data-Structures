dict = {0: 1}

def bsts(n):
    temp_ele = 0
    if num not in dict:
        for i in range(1, num+1):
            temp_ele += (bsts(i-1) * bsts(num-i))
            dict[num] = temp_ele
    return dict[num]

    


