# # task 1
import sys
sys.setrecursionlimit(200005)
N, M = map(int, input().split(" "))
li = [[] for i in range(N+1)]
for i in range(M):
    s, e = map(int, input().split(" "))
    li[s].append(e)

def topological(graph, vis, curr, stack, in_stack, has_cycle):
    vis[curr] = True
    in_stack[curr] = True
    for i in range(len(graph[curr])):
        edge = graph[curr][i]
        if in_stack[edge]:
            has_cycle[0] = True
        if vis[edge] != True:
            topological(graph, vis, edge, stack, in_stack, has_cycle)
    in_stack[curr] = False
    stack.append(curr)
vis = [False for i in range(N+1)]
stack = []
in_stack = [False for i in range(N+1)]
has_cycle = [False]

for i in range(1, N+1):
    if vis[i] == False:
        topological(li, vis, i, stack, in_stack, has_cycle)
if has_cycle[0]:
    print(-1)
else:
    st = stack[::-1]
    print(*st)

# task 2
from collections import deque
N, M = map(int, input().split(" "))
li = [[] for i in range(N+1)]
for i in range(M):
    s, e = map(int, input().split(" "))
    li[s].append(e)
    li[e].append(s)

def bipartite(graph):
    colors = [-1 for i in range(len(graph))]
    robots = 0
    for i in range(1, len(graph)):
        if colors[i] != -1:
            continue
        color_0 = 0
        color_1 = 0
        Q = deque()
        Q.append(i)
        colors[i] = 0
        color_0 = color_0 + 1

        while Q:
            curr = Q.popleft()
            current = colors[curr]

            for edge in graph[curr]:
                if colors[edge] == -1:
                    colors[edge] = 1 - current
                    if colors[edge] == 0:
                        color_0 += 1
                    else:
                        color_1 += 1
                    Q.append(edge)
        
        robots += max(color_0, color_1)
    humans = N - robots
    
    res = max(robots, humans)
    print(res)

bipartite(li)

# task 4

import sys
sys.setrecursionlimit(2 * 10**5 + 5)

n, r = map(int, input().split())
adj = [[] for i in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
s = [0] * (n + 1)

def dfs(x, p):
    s[x] = 1
    for y in adj[x]:
        if y != p:
            dfs(y, x)
            s[x] += s[y]

dfs(r, -1)

q = int(input())
for i in range(q):
    x = int(input())
    print(s[x])

# task 5

from collections import deque

n=int(input())
g=[[] for i in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(s):
    q=deque([(s,0)])
    v={s}
    fn=s
    md=0
    while q:
        x,cd=q.popleft()
        if cd>md:
            fn,md=x,cd
        for i in g[x]:
            if i not in v:
                v.add(i)
                q.append((i,cd+1))
    return fn,md

a,i= bfs(1)
b,l= bfs(a)
print(l)
print(a,b)

# task 6

def topological_sort(graph, vertices):
    s = {x: 0 for x in vertices}
    r = []
    def dfs(n):
        if s[n] == 1: return False
        if s[n] == 2: return True
        s[n] = 1
        for c in sorted(graph[n]):
            if not dfs(c):
                return False
        s[n] = 2
        r.append(n)
        return True
    for v in sorted(vertices):
        if s[v] == 0 and not dfs(v):
            return None
    return r[::-1]

def find_order(words):
    g = {c: [] for c in 'abcdefghijklmnopqrstuvwxyz'}
    used_chars = set(''.join(words))
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        m = min(len(w1), len(w2))
        p = True
        for j in range(m):
            if w1[j] != w2[j]:
                g[w1[j]].append(w2[j])
                p = False
                break
        if p and len(w1) > len(w2):
            return "-1"
    
    vertices = list('abcdefghijklmnopqrstuvwxyz')
    order = topological_sort(g, vertices)
    
    if not order:
        return "-1"
    
    used_in_graph = set()
    for c in order:
        if c in used_chars or any(g[c]) or any(c in g[x] for x in g):
            used_in_graph.add(c)
    
    final_order = [c for c in order if c in used_in_graph]
    unused = sorted(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in used_in_graph)
    return ''.join(final_order + unused)

n = int(input())
words = [input().strip() for _ in range(n)]
f = find_order(words)
print(f)

# task 3

from collections import deque
N = int(input())
visited = [[-1 for i in range (N+1)] for i in range(N+1)]
s1,s2,d1,d2 = map(int, input().split())
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
def knight():
    q = deque()
    q.append((s1, s2))
    visited[s1][s2] = 0
    while q:
        u = q.popleft()
        x,y = u[0], u[1]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 1<= nx <= N and 1<= ny <= N and visited[nx][ny] == -1:
                visited[nx][ny] =  visited[x][y] + 1
                if nx == d1 and ny == d2:
                    return visited[nx][ny]
                q.append((nx, ny))
    return -1
if s1 == d1 and s2 == d2:
    print(0)
else:
    print(knight())

# task 6

def sub_str(p, s):
    if len(p) < len(s):
        return False
    for i in range(min(len(p), len(s))):
        if p[i] != s[i]:
            return False
    return True

def bfs(g, d, t):
    from queue import PriorityQueue
    q = PriorityQueue()
    for i in range(26):
        if d[i] == 0:
            q.put(-i)
    r = ""
    while not q.empty():
        a = -q.get()
        t -= 1
        r += chr(a + ord('a'))
        for u in g[a]:
            d[u] -= 1
            if d[u] == 0:
                q.put(-u)
    print(r if t == 0 else "-1")

def solve():
    n = int(input())
    p = input()
    g = [[] for _ in range(26)]
    d = [-1] * 26
    t = 0
    while n > 1:
        s = input()
        if sub_str(p, s):
            print("-1")
            return
        f = True
        for i in range(max(len(p), len(s))):
            u = v = -1
            if i < len(p):
                u = ord(p[i]) - ord('a')
                if d[u] == -1:
                    d[u] = 0
                    t += 1
            if i < len(s):
                v = ord(s[i]) - ord('a')
                if d[v] == -1:
                    d[v] = 0
                    t += 1
            if f and i < min(len(s), len(p)) and s[i] != p[i]:
                f = False
                g[u].append(v)
                d[v] += 1
        p = s
        n -= 1
    bfs(g, d, t)

if __name__ == "__main__":
    solve()
    

