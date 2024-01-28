
from math import ceil

def sort(NumArr):
    Sorted_Arr = []
    while NumArr:
        min_value,index = NumArr[0][0],0
        for i in NumArr:
            if i[0]<min_value:
                min_value = i[0]
                index = NumArr.index(i)
        Sorted_Arr.append(min_value)
        NumArr[index].pop(0)
        if not NumArr[index]:
            NumArr.remove(NumArr[index])     
    return Sorted_Arr

def kmergesort(ArrNum, k):
    if len(ArrNum) == 1: 
        return ArrNum

    j = ceil(len(ArrNum)/k) 

    ArrNum = [kmergesort(ArrNum[i:i+j], k) for i in range(0, len(ArrNum), j)]

    return sort(ArrNum) 

if __name__ == "__main__":
    list = [1,20,3,4,-5,6,70,8,9]
   