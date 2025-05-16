# # task 1
import heapq

n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

g = [[] for i in range(n + 1)]
for i in range(m):
    g[u[i]].append((v[i], w[i]))

dist = [float('inf')] * (n + 1)
par = [-1] * (n + 1)
dist[s] = 0

pq = [(0, s)]

while pq:
    cost, node = heapq.heappop(pq)
    if cost > dist[node]:
        continue
    for nei, wt in g[node]:
        if dist[node] + wt < dist[nei]:
            dist[nei] = dist[node] + wt
            par[nei] = node
            heapq.heappush(pq, (dist[nei], nei))

if dist[d] == float('inf'):
    print(-1)
else:
    print(dist[d])
    path = []
    while d != -1:
        path.append(d)
        d = par[d]
    print(*path[::-1])

# # task 2

import heapq

def dijk(n, g, src):
    d = [float('inf')] * (n + 1)
    d[src] = 0
    pq = [(0, src)]
    while pq:
        c, u = heapq.heappop(pq)
        if c > d[u]: continue
        for v, w in g[u]:
            if d[v] > c + w:
                d[v] = c + w
                heapq.heappush(pq, (d[v], v))
    return d

n, m, s, t = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

da = dijk(n, g, s)
db = dijk(n, g, t)

ans = float('inf')
meet = -1

for i in range(1, n + 1):
    if da[i] == float('inf') or db[i] == float('inf'):
        continue
    mx = max(da[i], db[i])
    if mx < ans:
        ans = mx
        meet = i
    elif mx == ans and i < meet:
        meet = i

if meet == -1:
    print(-1)
else:
    print(ans, meet)

# task 3

import heapq

def min_danger(n, m, roads):
    g = [[] for i in range(n + 1)]
    for u, v, w in roads:
        g[u].append((v, w))
        g[v].append((u, w))

    d = [float('inf')] * (n + 1)
    d[1] = 0
    pq = [(0, 1)]

    while pq:
        cd, u = heapq.heappop(pq)
        if cd > d[u]:
            continue
        for v, w in g[u]:
            nd = max(cd, w)
            if nd < d[v]:
                d[v] = nd
                heapq.heappush(pq, (nd, v))

    res = []
    for i in range(1, n + 1):
        res.append(-1 if d[i] == float('inf') else d[i])
    return res

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for i in range(m)]
ans = min_danger(n, m, roads)
print(' '.join(map(str, ans)))

# task 4

import heapq

def min_cost(n, m, s, d, w, edges):
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)

    dist = [float('inf')] * (n + 1)
    dist[s] = w[s - 1]
    pq = [(dist[s], s)]

    while pq:
        c, u = heapq.heappop(pq)
        if c > dist[u]:
            continue
        for v in g[u]:
            nc = c + w[v - 1]
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))

    return dist[d] if dist[d] != float('inf') else -1

n, m, s, d = map(int, input().split())
w = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for i in range(m)]
print(min_cost(n, m, s, d, w, edges))

# task 5

import heapq

def solve(n, m, u, v, w):
    g = [[] for i in range(n + 1)]
    for i in range(m):
        g[u[i]].append((v[i], w[i]))

    d = [[float('inf')] * 2 for i in range(n + 1)]
    pq = [(0, 1, -1)]

    while pq:
        c, x, p = heapq.heappop(pq)
        for y, wt in g[x]:
            np = wt % 2
            if np == p:
                continue
            if c + wt < d[y][np]:
                d[y][np] = c + wt
                heapq.heappush(pq, (c + wt, y, np))

    res = min(d[n])
    return res if res != float('inf') else -1

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
print(solve(n, m, u, v, w))

# task 6

import heapq

def second_shortest_path(n, m, s, d):
    g = [[] for i in range(n + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))

    inf = float('inf')
    dist = [[inf, inf] for i in range(n + 1)]
    dist[s][0] = 0

    pq = [(0, s)]

    while pq:
        c, u = heapq.heappop(pq)
        for v, w in g[u]:
            new_c = c + w
            if new_c < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = new_c
                heapq.heappush(pq, (new_c, v))
            elif dist[v][0] < new_c < dist[v][1]:
                dist[v][1] = new_c
                heapq.heappush(pq, (new_c, v))

    return dist[d][1] if dist[d][1] != inf else -1

n, m, s, d = map(int, input().split())
print(second_shortest_path(n, m, s, d))



