# task 1
n, k = map(int, input().split())
p = list(range(n + 1))
sz = [1] * (n + 1)

def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]

for i in range(k):
    a, b = map(int, input().split())
    x, y = f(a), f(b)
    if x != y:
        if sz[x] < sz[y]:
            x, y = y, x
        p[y] = x
        sz[x] += sz[y]
    print(sz[f(x)])

# task 2

n, m = map(int, input().split())
e = []
for _ in range(m):
    u, v, w = map(int, input().split())
    e.append((w, u, v))
e.sort()
p = list(range(n + 1))

def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]

res = 0
for w, u, v in e:
    x, y = f(u), f(v)
    if x != y:
        p[y] = x
        res += w
print(res)

# task 3
class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.sz = [1] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.sz[pa] > self.sz[pb]:
            self.p[pb] = pa
            self.sz[pa] += self.sz[pb]
        else:
            self.p[pa] = pb
            self.sz[pb] += self.sz[pa]
        return True

def get_edges(m):
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    return edges

def mst(n, edges, tree, excl):
    dsu = DSU(n)
    cost, total = 0, 0
    for i, (w, u, v) in enumerate(edges):
        if dsu.unite(u, v):
            cost += w
            total += 1
            tree.append(i)
        else:
            excl.append(i)
    return cost if total == n - 1 else -1

def second_mst(n, edges, tree, excl, skip_idx, mst_cost):
    dsu = DSU(n)
    cost, total = 0, 0
    for i in tree:
        if i == skip_idx:
            continue
        w, u, v = edges[i]
        dsu.unite(u, v)
        cost += w
        total += 1
    for i in excl:
        w, u, v = edges[i]
        if w == edges[skip_idx][0]:
            continue
        if dsu.unite(u, v):
            cost += w
            total += 1
            if total == n - 1:
                return cost if cost > mst_cost else -1
    return -1

def solve():
    n, m = map(int, input().split())
    edges = get_edges(m)
    tree, excl = [], []
    min_cost = mst(n, edges, tree, excl)
    if min_cost == -1:
        print(-1)
        return
    ans = float('inf')
    for idx in tree:
        sc = second_mst(n, edges, tree, excl, idx, min_cost)
        if sc != -1:
            ans = min(ans, sc)
    print(ans if ans != float('inf') else -1)

solve()
