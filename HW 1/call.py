from random import randint

def qsort(ArrayNum):
    if (len(ArrayNum) == 0):
        return []
    else:
        pivot = ArrayNum[0]

        left =  [i for i in ArrayNum if i < pivot ]
        right = [j for j in ArrayNum[1:] if j >= pivot ]

    return [qsort(left)] + [pivot] + [qsort(right)]

def traverse(tree):
    def _search(tree):
        if tree == []:
            return 0,0

        left_ele,cur_left = _search(tree[0])
        right_ele,cur_right = _search(tree[2])
        str = max(left_ele,right_ele) + 1
        curve = max(cur_left,cur_right)
        curve = max(curve,left_ele + right_ele)
        return str,curve
    str,curve = _search(tree)
    return max(curve,str-1)
    


      ##def search_tree(tree,):
      ##    sub_set =_search(tree,key)
      ##    if sub_set != []:
      ##        return True
      ##    else:
      ##        return False


if __name__ == "__main__":
    Int_Array = ([100,98,50,55,60,65,70,80,105,110])  
    tree = qsort(Int_Array)
    print("Sorted tree After Qsort is {}".format(tree))
    result = traverse(tree)
    print(result)