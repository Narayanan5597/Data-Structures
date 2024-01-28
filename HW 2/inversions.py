def Merging(Num_Array, left_ele, mid_ele, right_ele):
    i = left_ele
    j = mid_ele
    k = 0
    Count = 0
    Temp_Array = [0 for x in range(right_ele - left_ele + 1)]
 
    while (i < mid_ele) and (j <= right_ele):
        if Num_Array[i] <= Num_Array[j]:
            Temp_Array[k] = Num_Array[i]
            k += 1
            i += 1
 
        else:
            Temp_Array[k] = Num_Array[j]
            Count += mid_ele - i
            k += 1
            j += 1
 
    while i < mid_ele:
        Temp_Array[k] = Num_Array[i]
        k += 1
        i += 1
 
    while j <= right_ele:
        Temp_Array[k] = Num_Array[j]
        k += 1
        j += 1
 
    k = 0
    for i in range(left_ele, right_ele + 1):
        Num_Array[i] = Temp_Array[k]
        k += 1
 
    return Count
 
 
def mergeSort(Num_Array, left_ele, right_ele):
    Count = 0
 
    if right_ele > left_ele:
        mid_ele = (right_ele + left_ele) // 2
 
        Count = mergeSort(Num_Array, left_ele, mid_ele)
        Count += mergeSort(Num_Array, mid_ele + 1, right_ele)
        Count += Merging(Num_Array, left_ele, mid_ele + 1, right_ele)
 
    return Count
 
def num_inversions(Num_Array):
    left = 0
    right_ele = len(Num_Array)-1
    inv_count = mergeSort(Num_Array,left,right_ele)
    return inv_count 


Num_Array = [2, 4, 1, 3]
inv_count = num_inversions(Num_Array)
print(inv_count)
