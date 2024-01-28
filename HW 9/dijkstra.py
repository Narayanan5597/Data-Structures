from collections import defaultdict
from heapdict import heapdict
from time import time


def shortest(n, edges):
    graph = defaultdict(dict)
    for (u, v, w) in edges:
        graph[u][v] = w
        graph[v][u] = w

    heap = heapdict()
    for i in range(n):
        heap[i] = float("inf")
    heap[0] = 0
    back = defaultdict(int)

    while True:
        v, w = heap.popitem()
        distance = w
        if v == n - 1:
            break

        for u, cost in graph[v].items():
            if u in heap and heap[u] > w + cost:
                heap[u] = w + cost
                back[u] = v

    if distance == float("inf"):
        return None
    #  backtrack the shortest path
    path, distance_index = [], n - 1
    path.append(n - 1)
    path[:0] = [back[distance_index]]
    while back[distance_index] != 0:
        distance_index = back[distance_index]
        path[:0] = [back[distance_index]]

   
    return distance, path

if __name__ == "__main__":
    print(shortest(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))