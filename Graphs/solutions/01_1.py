graph = {}

[N, E] = [int(x) for x in input().split()]

for i in range(N):
    v = int(input())
    graph[v] = []

for i in range(E):
    [e1, e2] = [int(x) for x in input().split()]
    graph[e1].append(e2)
    graph[e2].append(e1)

visited = set() # Set to keep track of visited nodes of graph.

def dfs(graph, v, visited, parent): 
    visited.add(v)

    for neighbor in graph[v]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, v):
                return True
        elif neighbor != parent:
            return True
        
    return False


print(dfs(graph, 1, visited, -1))
