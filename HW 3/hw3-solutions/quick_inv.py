import sys

def count_inversions(a):

    count = 0
    
    def sort(a):
        if a == []:
            return []
        
        pivot = a[0]
        left = []
        for i in range(len(a)):
            if a[i] < pivot:
                left.append(a[i])
                nonlocal count
                count = count + abs(i-len(left) + 1)
                
        right = [x for x in a[1:] if x >= pivot]

        return sort(left) + [pivot] + sort(right)
    sorted_arr = sort(a)

    return count


if __name__ == "__main__":
    print(count_inversions([4,1,3,2]))