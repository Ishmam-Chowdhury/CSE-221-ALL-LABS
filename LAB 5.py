# #task 1
from collections import deque 
N, M = map(int, input().split(" "))
li = [[] for i in range(N)]
for i in range(M):
    s, e = map(int, input().split(" "))
    s -= 1
    e -= 1
    li[s].append(e)
    li[e].append(s)

def bfs(graph):
    vis = [False for i in range(len(graph))]
    Q = deque()
    Q.append(0)
    while Q:
        curr = Q.popleft()
        if vis[curr] == False:
            print(curr + 1, end=" ")
            vis[curr] = True
            for i in range(len(graph[curr])):
                e = graph[curr][i]
                Q.append(e)

bfs(li)

# task 2

import sys
sys.setrecursionlimit(2 * 10**5 + 5)
N, M = map(int, input().split())
u_nodes = list(map(int, input().split()))
v_nodes = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = u_nodes[i], v_nodes[i]
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N + 1):
    graph[i].sort() 

vis = [False] * (N + 1)

def dfs(u):
    print(u, end=" ")
    vis[u] = True
    for v in graph[u]:
        if vis[v] == False:
            dfs(v)

dfs(1)

# task 5

import sys
sys.setrecursionlimit(2*100000+5)

cycle = False

def dfs(graph, vst, rec, at):
    global cycle
    vst[at] = 1
    rec[at] = True
    for u in graph[at]:
        if vst[u] == 0:
            dfs(graph, vst, rec, u)
        elif rec[u]:
            cycle = True
    rec[at] = False

def solve():
    global cycle
    cycle = False
    n, m = list(map(int, input().split()))
    graph = [[] for i in range(n+1)]
    for i in range(m):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
    
    visited = [0]*(n+1)
    rec = [False]*(n+1)
    for u in range(1, n+1):
        if visited[u] == 0:
            dfs(graph, visited, rec, u)
    
    if cycle:
        print("YES")
    else:
        print("NO")

solve()

# task 3

from collections import deque

N, M, S, D = map(int, input().split())
u_nodes = list(map(int, input().split()))
v_nodes = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = u_nodes[i], v_nodes[i]
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort()

def bfs(graph, S, D, N):
    vis = [False] * (N + 1)
    parent = [-1] * (N + 1)
    Q = deque()
    Q.append(S)
    vis[S] = True
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if not vis[v]:
                vis[v] = True
                parent[v] = u
                Q.append(v)
    if not vis[D]:
        print(-1)
        return
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    print(len(path) - 1)
    print(*path[::-1])

if S == D:
    print(0)
    print(S)
else:
    bfs(graph, S, D, N)


