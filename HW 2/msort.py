def mergesort(Number_Array):


    if len(Number_Array) > 1:
        Mid_element = len(Number_Array) // 2  
        left_element = Number_Array[:Mid_element]  
        right_element = Number_Array[Mid_element:] 

        mergesort(left_element)
        mergesort(right_element)

        i = j = k = 0

        
        while i < len(left_element) and j < len(right_element):
            if left_element[i] < right_element[j]:
                Number_Array[k] = left_element[i]
                i = i + 1
            else:
                Number_Array[k] = right_element[j]
                j = j + 1
            k = k + 1

        
        while i < len(left_element):
            Number_Array[k] = left_element[i]
            i = i + 1
            k = k + 1

        while j < len(right_element):
            Number_Array[k] = right_element[j]
            j = j + 1
            k = k + 1

    return Number_Array




if __name__ == '__main__':
    array = [4, 2, 5, 1, 6, 3]
    print("Given array is", end="\n")
    print (array) 
    Sorted_array = mergesort(array)
    print("Sorted array is: ", end="\n")
    print(Sorted_array)     
    