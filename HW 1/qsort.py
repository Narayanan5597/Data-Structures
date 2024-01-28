
from random import randint

def qsort(ArrayNum):
    if (len(ArrayNum) == 0):
        return []
    else:
        pivot = ArrayNum[0]

        left =  [i for i in ArrayNum if i < pivot ]
        right = [j for j in ArrayNum[1:] if j >= pivot ]

    return [qsort(left)] + [pivot] + [qsort(right)]

def _search(tree,find_element):
    if tree == []:
        return tree
    else:
        tot_len = len(tree) - 1
        if tree[tot_len-1] == find_element:
            return tree
        elif tree[1]< find_element:
            return _search(tree[tot_len],find_element)
        else:
            return _search(tree[tot_len-2],find_element)


def insert_node(tree,key):
    
    sub_set = _search(tree,key)
    if sub_set == []:
        sub_set.extend([[],[key],[]])

def sorted(tree):
    if tree:
       return sorted(tree[0]) + [tree[1]] + sorted(tree[2])
    else:
        return []        
    
def search_tree(tree,key):
    sub_set =_search(tree,key)
    if sub_set != []:
        return True
    else:
        return False


if __name__ == "__main__":
    Int_Array = ([9,44,2,6,3,5,7,1,9])  
    tree = qsort(Int_Array)
    print("Sorted tree After Qsort is {}".format(tree))
    result = search_tree(tree,44)
    print("Search Result is {}".format(result))
    print("Insertion Operation")
    insert_node(tree, 1.5)
    print("Sorted tree to List")
    print (tree)
    sorted_list = sorted(tree)
    print(sorted_list)
 




