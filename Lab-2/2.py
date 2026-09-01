from collections import deque

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

# 1. DEPTH-FIRST SEARCH (Recursive - Dives Deep First)
def dfs_rec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i, res)


def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfs_rec(adj, visited, 0, res)  # Start from node 0
    return res


# 2. BREADTH-FIRST SEARCH (Queue-based - Explores Level by Level)
def bfs(adj):
    visited = [False] * len(adj)
    res = []
    
    q = deque()
    src = 0
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res

if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]

    # Adding edges
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 0, 4)  
    add_edge(adj, 2, 3)

    # Perform DFS and BFS starting from node 0
    dfs_res = dfs(adj)
    bfs_res = bfs(adj)

    print("DFS Traversal:", *dfs_res)
    print("BFS Traversal:", *bfs_res)