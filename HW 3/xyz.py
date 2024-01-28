def find(array):
    array = sorted(array)
    # print(arr)
    triplet_array = []
    for  initial_ele in array: #n

        start = 0
        final = len(array) -1 

        while start < final: # n^2
            result = array[start] + array[final]
            if result < initial_ele:
                start = start + 1
            elif result > initial_ele:
                final = final - 1
            else:
                triplet_array.append((array[start], array[final], initial_ele))
                start = start + 1
                final = final - 1

    return triplet_array




if __name__ == "__main__":
    arr = [1, 4, 2, 3, 5]
    print(find(arr))