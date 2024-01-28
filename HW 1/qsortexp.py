from random import randint

def quicksort(Numlist,start,last):
    if ((last - start )>0):
      
        pivot_index = partition(Numlist,start,last)
        quicksort(Numlist,start,pivot_index-1)
        quicksort(Numlist,pivot_index+1,last)
        return Numlist


def partition(ArrNum,beg,end):
    pivot = end
    pointer = beg
    for i in range(beg,end):
        if(ArrNum[i] < ArrNum[pivot]):
          ArrNum[i],ArrNum[pointer] = ArrNum[pointer],ArrNum[i] 
          pointer += 1
    ArrNum[pivot],ArrNum[pointer] = ArrNum[pointer],ArrNum[pivot]
    return pointer

Arrlist = [4,1,-5,2,9,0,4,1,7,3,8]
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)





        




