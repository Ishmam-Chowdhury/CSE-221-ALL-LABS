# #task 1
N, M = map(int, input().split(" "))
li = [[int(0) for i in range(N)] for i in range(N)] 
for i in range(M):
    s, e, w = map(int, input().split(" "))
    s -= 1
    e -= 1
    li[s][e] = w

for i in range(N):
    print(" ".join(str(x) for x in li[i]))

#task 3

N = int(input())
mat = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
    ver = input().split(" ")
    v = int(ver[0])
    for j in range(1, v + 1):
        mat[i][int(ver[j])] = 1
for i in range(N):
    print(" ".join(str(x) for x in mat[i]))

# task 4
N, M = map(int, input().split(" "))
l1 = input().split(" ")
l2 = input().split(" ")

lis = [int(0) for i in range(N+1)]
for i in range(M):
    if int(l1[i]) == int(l2[i]):
        lis[int(l1[i])] += 1
    else:
        lis[int(l1[i])] += 1
        lis[int(l2[i])] += 1
odd = 0
for i in range(1, N + 1):
    if lis[i] % 2 != 0:
        odd += 1

if odd == 0 or odd == 2:
    print("YES")
else:
    print("NO")

# task 5

N, M = map(int, input().split(" "))
l1 = input().split(" ")
l2 = input().split(" ")
lis = [int(0) for i in range(N+1)]
for i in range(M):
    lis[int(l1[i])] -= 1
    lis[int(l2[i])] += 1
print(" ".join(str(lis[x]) for x in range(1,len(lis))))

# task 6

N = int(input())
x, y = input().split(" ")
x, y = int(x), int(y)

lis = [
    [x-1, y-1], [x-1, y], [x-1, y+1],
    [x, y-1], [x, y+1],
    [x+1, y-1], [x+1, y], [x+1, y+1]
]

i = 0
while i < len(lis):
    a = lis[i][0]
    b = lis[i][1]
    if (a < 1 or a > N) or (b < 1 or b > N) :
        lis.remove(lis[i])
        if i > len(lis):
            break
        i -= 1
    i += 1
print(len(lis))
for i in lis:
    print(f"{i[0]} {i[1]}")

# task 7

from math import gcd

N, Q = map(int, input().split(" "))
lis = []
for i in range(Q):
    x, y = map(int, input().split(" "))
    l = [x, y]
    lis += [l]
nodes = [[] for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if gcd(i, j) == 1:
            nodes[i].append(j)
    if i == 1 and nodes[i][0] == 1:
        nodes[i].remove(1)
for j in lis:
    x, k = j

    l1 = nodes[x]
    
    if len(l1) < k:
        print(-1)
    else:
        print(l1[k-1])

# task 2

N,M = map(int, input().split(" "))
s = list(map(int, input().split(" ")))
e = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
graph = [[] for i in range(N+1)]

for i in range(M):
    graph[s[i]].append((e[i], w[i]))

for i in range(1, N + 1):
    print(f"{i}:", end=" ")
    for e, w in graph[i]:
        print(f"({e},{w})", end=" ")
    print()



