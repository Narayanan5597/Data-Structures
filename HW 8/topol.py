from collections import defaultdict 
def order(n, edg):
    def visit(v):
        if v in visited: 
            return 
        visited.add(v)
        for u in prereqs[v]:
            visit(u) 
        output.append(v) 

    graph   = defaultdict(list) 
    prereqs = defaultdict(list)

    for u, v in edg: 
        graph[u].append(v)
        prereqs[v].append(u)

    nodes = range(n)
    output = []
    visited = set()
    for v in nodes:
        visit(v)

    return output 

##print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))

##print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))

