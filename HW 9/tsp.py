from collections import defaultdict
import copy
from time import time


def insert_vertex(n, v, bits):
    if v == -1:
        return bits + 1
    else:
        return bits + 2 ** (n - v)


def remove_vertex(n, v, bits):
    if v == -1:
        return bits - 1
    else:
        return bits - 2 ** (n - v)


def tsp(n, edges):
    graph = defaultdict(dict)
    for (u, v, w) in edges:
        graph[u][v] = w
        graph[v][u] = w
        if u == 0:
            graph[-1][v] = w
            graph[v][-1] = w
        if v == 0:
            graph[u][-1] = w
            graph[-1][u] = w

    opt = defaultdict(dict)
    back = defaultdict(dict)

    def tsp_helper(vsted_bit, i):
        if vsted_bit == 2**n and i == 0:
            return 0
        if i in opt[vsted_bit]:
            return opt[vsted_bit][i]
        min_cost = float("inf")
        for v in range(n):
            if 2 ** (n - v) & vsted_bit != 0:
                if v != i and v in graph[i]:
                    new_vstd_bit = remove_vertex(n, i, vsted_bit)
                    temp = tsp_helper(new_vstd_bit, v)
                    if temp is not None and min_cost > temp + graph[v][i]:
                        min_cost = temp + graph[v][i]
                        back[vsted_bit][i] = v

        if min_cost == float("inf"):
            opt[vsted_bit][i] = None
        else:
            opt[vsted_bit][i] = min_cost
        return opt[vsted_bit][i]

    def solution(visited_bit, i):
        if visited_bit == 2**n and i == 0:
            return [0]
        vertex = back[visited_bit][i]
        new_vstd_bit = remove_vertex(n, i, visited_bit)
        if i == -1:
            i = 0
        return solution(new_vstd_bit, vertex) + [i]

    vertices_bit = 0
    for i in range(n):
        vertices_bit = insert_vertex(n, i, vertices_bit)
    vertices_bit = insert_vertex(n, -1, vertices_bit)

    return tsp_helper(vertices_bit, -1), solution(vertices_bit, -1)


# print(tsp(2, [(0, 1, 1)]))
# print(tsp(3, [(0, 1, 1), (1, 2, 2), (0, 2, 3)]))
# print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
# print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6), (3, 0, 1)]))
print(
    tsp(
        16,
        [
            (1, 2, 0),
            (11, 5, 5),
            (9, 8, 4),
            (6, 1, 4),
            (5, 13, 5),
            (12, 11, 4),
            (14, 8, 0),
            (0, 11, 3),
            (10, 12, 3),
            (5, 5, 1),
            (7, 0, 1),
            (10, 5, 1),
            (11, 5, 3),
            (13, 11, 4),
            (11, 11, 3),
            (5, 12, 5),
            (14, 7, 3),
            (8, 15, 4),
            (11, 14, 3),
            (11, 14, 3),
            (7, 10, 5),
            (5, 8, 3),
            (9, 9, 5),
            (13, 9, 5),
            (6, 15, 4),
            (11, 2, 2),
            (0, 6, 5),
            (3, 1, 4),
            (1, 8, 4),
            (7, 3, 4),
            (4, 8, 1),
            (6, 1, 3),
            (1, 1, 2),
            (11, 5, 1),
            (0, 2, 0),
            (2, 0, 0),
            (0, 11, 2),
            (4, 5, 5),
            (5, 0, 3),
            (1, 7, 1),
            (1, 0, 2),
            (3, 9, 2),
            (15, 0, 2),
            (14, 1, 2),
            (12, 4, 3),
            (7, 2, 5),
            (10, 3, 0),
            (14, 4, 4),
            (12, 15, 4),
            (10, 4, 2),
            (8, 8, 4),
            (13, 0, 5),
            (4, 1, 2),
            (1, 4, 1),
            (5, 3, 3),
            (7, 1, 1),
            (7, 14, 0),
            (8, 2, 4),
            (7, 11, 2),
            (13, 8, 4),
            (0, 4, 0),
            (12, 13, 1),
            (3, 2, 1),
            (3, 3, 0),
            (5, 7, 0),
            (6, 0, 4),
            (14, 14, 2),
            (12, 6, 5),
            (6, 13, 3),
            (0, 1, 3),
            (5, 3, 5),
            (15, 11, 0),
            (3, 11, 2),
            (11, 9, 0),
            (13, 3, 0),
            (9, 6, 5),
            (0, 14, 0),
            (13, 15, 3),
            (6, 2, 0),
            (9, 0, 2),
            (9, 2, 1),
            (15, 6, 0),
            (11, 12, 5),
            (14, 4, 2),
            (12, 3, 2),
            (3, 3, 0),
            (10, 12, 1),
            (3, 0, 4),
            (15, 1, 5),
            (15, 9, 2),
            (14, 4, 2),
            (8, 15, 4),
            (15, 13, 3),
            (9, 12, 1),
            (5, 15, 4),
            (8, 13, 5),
            (2, 3, 0),
            (11, 5, 4),
            (4, 13, 0),
            (2, 1, 1),
        ],
    )
)

(6, [0, 4, 8, 14, 7, 5, 10, 3, 13, 12, 9, 11, 15, 6, 2, 1, 0])
