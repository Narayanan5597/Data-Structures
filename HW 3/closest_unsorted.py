import enum
from random import randint
from collections import defaultdict

def find(array,x,k):
    result = []
    temp_array = []
    temp_array1 = []
   # new_list = []
   # new_list1 =[]
    
    hash_map = defaultdict(list)
    n = 0
    while n < len(array):
        temp_array.append( abs(x-array[n]))
        
        n = n+1
    temp_array1.extend(temp_array)
    for i,j in enumerate(temp_array):
        hash_map[j].append(i)
    #print(array)
    #print(temp_array1)
    #print(x)
    Quick_int = qselect(k,temp_array)
    final_abs = [i for i in temp_array if i <= Quick_int]
    for value in final_abs:
        result.extend(hash_map[value])
    
    return [array[i] for i in set(result)]


    
    
   ## #print(new_list3)
        
        
            
           
    # new_list.append(temp_array[i] )
    # new_list1.append(x-temp_array[i])
    # count = count + 1

    
   

        # elif(array[i]<x) & (temp_array[i] <= Quick_int):
        #      new_list.append(temp_array[i] )
        # else:
        #    break



        

     
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






find([4,1,3,2,7,4], 6.5, 3)






