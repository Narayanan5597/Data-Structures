from collections import defaultdict


def order(n, edg):
    topol = []
    in_degree = [0] * n
    graph = defaultdict(list)

    for (u, v) in edg:
        in_degree[v] += 1
        graph[u].append(v)
    que = []
    op = 0
    for i in range(n):
        if in_degree[i] == 0:
            que.append(i)

    while op != len(que):
        u = que[op]
        topol.append(u)
        op += 1

        adj = graph[u]
        for v in adj:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)

    if len(topol) != n:
        return None
    return topol


def longest(n, edg):

    in_degree = [0] * n
    dg = [0] * n
    back = [0] * n

    graph = defaultdict(list)

    for (u, v) in edg:
        in_degree[v] += 1
        graph[v].append(u)

    topol = order(n, edg)

    max_d, max_v = 0, 0
    for i in topol:
        if in_degree[i] != 0:
            adj = graph[i]
            for v in adj:
                if dg[i] < dg[v] + 1:
                    dg[i] = dg[v] + 1
                    back[i] = v
            if dg[i] > max_d:
                max_d = dg[i]
                max_v = i

    long_pth, v = [], max_v
    long_pth.append(v)
    while in_degree[v] != 0:
        v = back[v]
        long_pth[:0] = [v]

    return max_d, long_pth


##print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
##print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
##print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))