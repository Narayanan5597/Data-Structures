
from itertools import product
from traceback import print_tb
from random import *
import random

def nbesta(a ,b, n):
    Array = list(product(a,b))
    Array1 = sorted(Array, key=sum)
    return Array1[:n]


def Quick_Select(ArrayNum, k):
    pivot_index = random.randint(0, len(ArrayNum) - 1)
    l_ArrayNum = []
    r_ArrayNum = []
    for i in range(len(ArrayNum)):
        if i == pivot_index:
            continue
        elif ArrayNum[i] >= ArrayNum[pivot_index]:
            r_ArrayNum.append(ArrayNum[i])
        else:
            l_ArrayNum.append(ArrayNum[i])
    if len(l_ArrayNum) == k - 1:
        return ArrayNum[pivot_index]
    elif len(l_ArrayNum) > k - 1:
        return Quick_Select(l_ArrayNum, k)
    else:
        return Quick_Select(r_ArrayNum, k - len(l_ArrayNum) - 1)

def nbestb(a ,b, k):
    arr = list(product(a,b))
    sumarr = list(map(sum, arr))
    qsel = Quick_Select(sumarr, k)
    arr1 = []
    arr2 = []
    for i in range (0, len(sumarr)):
        if sumarr[i] < qsel:
            arr1.append(arr[i])
        elif sumarr[i] == qsel:
            arr2.append(arr[i])
    result = []
    itr = 0

    iter_a = 0
    iter_b = 0
    for n in range(0, k):

        while iter_a < len(arr1) and iter_b < len(arr2):
            if arr1[iter_a] < arr2[iter_b]:
                res_val = arr1[iter_a]
                result.append(res_val)
                iter_a += 1
            else:
                res_val = arr2[iter_b]
                result.append(res_val)
                iter_b += 1
        while iter_a < len(arr1):
            result.append(arr1[iter_a])
            iter_a += 1
        while iter_b < len(arr2):
            result.append(arr2[iter_b])
            iter_b += 1

    return result


def heappush(heap, e):
    heap.append(e)
    i = len(heap) - 1
    while i != 0:
        p = (i - 1) // 2
        if sum(heap[i][:2]) < sum(heap[p][:2]) or (sum(heap[i][:2]) == sum(heap[p][:2]) and heap[i][1] < heap[p][1]):
            heap[i], heap[p] = heap[p], heap[i]
        else:
            break
        i = p
        
def heappop(heap):
    a = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    i = 0
    while True:
        li = None
        hl = len(heap)
        l = (i * 2) + 1
        r = (i * 2) + 2
        if r < hl and l < hl:
            if sum(heap[l][:2]) > sum(heap[r][:2]):
                li = l
            elif sum(heap[l][:2]) < sum(heap[r][:2]):
                li = r
            else:
                if heap[l][-1] < heap[r][-1]:
                    li = l
                else:
                    li = r
        elif r >= hl and l < hl:
            li = l
        else:
            return a


        if sum(heap[i][:2]) > sum(heap[li][:2]):
            heap[i], heap[li] = heap[li], heap[i]
            i = li
        elif sum(heap[i][:2]) < sum(heap[li][:2]):
            return a
        else:
            if heap[i][-1] < heap[li][-1]:
                heap[i], heap[li] = heap[li], heap[i]
                i = li
            else:
                return a


def nbtestc(arr, arr1, n):
    arr = sorted(arr)
    arr1 = sorted(arr1)
    heap = []
    res = [[arr[0], arr1[0]]]

    if arr[0] + arr1[1] < arr[1] + arr1[0]:
        heap.append([arr[0], arr1[1], 0, 1])
        heap.append([arr[1], arr1[0], 1, 0])

    elif arr[0] + b[1] > arr[1] + arr1[0]:
        heap.append([arr[1], arr1[0], 1, 0])
        heap.append([arr[0], arr1[1], 0, 1])

    else:
        if arr1[0] < arr1[1]:
            heap.append([arr[1], arr1[0], 1, 0])
            heap.append([arr[0], arr1[1], 0, 1])
        else:
            heap.append([arr[0], arr1[1], 0, 1])
            heap.append([arr[1], arr1[0], 1, 0])

    while len(res) < n:
            ans = heappop(heap)
            res.append([ans[0], ans[1]])
            i, j = ans[2], ans[3]
            heappush(heap, [arr[i+1], arr1[j], i+1, j])
            heappush(heap, [arr[i], arr1[j+1], i, j+1])
    return res


    