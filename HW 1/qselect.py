from random import randint


def rand_partition(numlist,start,end):
    rand_num = randint(start,end)
    numlist[rand_num], numlist[end] = numlist[end],numlist[rand_num]
    return partition(numlist,start,end)


def qselect(k, Numlist):

    def quickselect(Numlist,start,last,k):
        if (start == last):
            return Numlist[start]
        if(start>last): 
            return Numlist[k]
        if k>len(Numlist):
            return 
        Numlist, pos = rand_partition(Numlist,start,last)
        nex_pos = pos - start + 1
        if(k == nex_pos):
            return Numlist[pos]
        elif k<nex_pos:
            return quickselect(Numlist,start,pos-1,k)
        else:
            return quickselect(Numlist,pos+1,last,k-nex_pos)
    start = 0
    last = len(Numlist) - 1
    return quickselect(Numlist,start,last,k)
        

        
def partition(ArrNum,beg,end):
    pivot = ArrNum[end]
    pointer = beg-1
    for i in range(beg,end):
        if(ArrNum[i] <= pivot):
            pointer += 1
            ArrNum[pointer],ArrNum[i] = ArrNum[i],ArrNum[pointer] 
          
    ArrNum[pointer + 1],ArrNum[end] = ArrNum[end],ArrNum[pointer + 1 ]
    return ArrNum, pointer+1



            
 
            