from random import randint

def quicksort(Numlist,start,last):
    if ((last - start )>0):
      if start < last:
      
        pivot = randint(start, last - 1)
        Numlist[pivot], Numlist[last] = (
            Numlist[last],
            Numlist[pivot],
        )
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

Arrlist = [4,99,2,-2,-111,1,-5,2,9,0,4,1,7,3,8]
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)
Arrlist = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print("\nOriginal list:")
print(Arrlist)
print("After applying Random Pivot Quick Sort the said list becomes:")
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)
Arrlist = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(Arrlist)
print("After applying Random Pivot Quick Sort the said list becomes:")
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)
Arrlist = [1.1, 1, 0, -1, -1.1, .1]
print("\nOriginal list:")
print(Arrlist)
print("After applying Random Pivot Quick Sort the said list becomes:")
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)
Arrlist = ['z','a','y','b','x','c']
print("\nOriginal list:")
print(Arrlist)
print("After applying Random Pivot Quick Sort the said list becomes:")
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)
Arrlist = ['z','a','y','b','x','c']
print("\nOriginal list:")
print(Arrlist)
print("After applying Random Pivot Quick Sort the said list becomes:")
quicksort(Arrlist,0,len(Arrlist)-1)
print(Arrlist)