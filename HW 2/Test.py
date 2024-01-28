from random import randint

## to sort the Array_numnbers using quicksort
def qsort(Array_Numbers):
    if (len(Array_Numbers) == 0):
        return []
    else:
        pivot = Array_Numbers[0]

        left =  [i for i in Array_Numbers if i < pivot ]
        right = [j for j in Array_Numbers[1:] if j >= pivot ]

    return [qsort(left)] + [pivot] + [qsort(right)]

#to find the longest path in the given tree structure
# the longest path can be found in two ways one is traversing in linear manner and the other is traversing in the curved path
# I have used the max function to find the largest between the linear tree ( stright direction tree) and curved tree and return the path 

def longest(Tree):
   
    def traverse(Tree):
        if Tree == []:
           
            return 0,0

        Left_Root,Left_Node = traverse(Tree[0])
       
        Right_Root,Right_Node = traverse(Tree[2])
       
        Curved_tree_Pointer = max(Left_Node,Right_Node)
       
        Straight_Longest_Root = max(Left_Root,Right_Root) + 1
        
        Curved_Longest_Root = max(Curved_tree_Pointer,Left_Root + Right_Root)
       
        return Straight_Longest_Root,Curved_Longest_Root
    
    straight_tree,curve_tree = traverse(Tree)

    return max(straight_tree-1,curve_tree)
    


     


if __name__ == "__main__":
    Int_Array = ([100,98,50,55,60,65,70,80,105,110])  
    Tree = qsort(Int_Array)
    print("Sorted tree After Qsort is {}".format(Tree))
    result = longest(Tree)
    print(result)

    result = longest([[[], 1, []], 2, [[], 3, []]])
    print(result)





   
    