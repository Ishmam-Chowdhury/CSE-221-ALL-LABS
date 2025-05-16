# # #A

n1 = [int(x) for x in input().split(" ")]
s=n1[1]
li = [int(x) for x in input().split(" ")]
i = 0
j = len(li) -1
while i<j:
  cur_sum = li[i] + li[j]
  if cur_sum<s:
    i+=1
  elif cur_sum>s:
    j-=1
  elif cur_sum == s:
    print(f"{i+1} {j+1}")
    break
  else:
    print(-1) 
    break
if i == j:
  print(-1)

# #B

n = int(input())
arr1 = [int(x) for x in input().split(" ")]
m = int(input())
arr2 = [int(x) for x in input().split(" ")]
res = []
i, j = 0, 0
while i<n and j<m:
  if arr1[i] < arr2[j]:
    res.append(arr1[i])
    i+=1
  else:
    res.append(arr2[j])
    j+=1
if j <m:
  res.extend(arr2[j:])
elif i<n:
  res.extend(arr1[i:])
for i in range(len(res)-1):
    print(res[i], end=" ")
print(res[len(res)-1])

#C

n, k = [int(x) for x in input().split(" ")]
arr = [int(x) for x in input().split(" ")]
i, j = 0,0
ma= 0
cur_sum = 0
while j < n:
  if cur_sum + arr[j]<= k:
    cur_sum += arr[j]
    ma = max(ma, j-i+1)
    j+=1
  elif cur_sum != 0:
    cur_sum-= arr[i]
    i+=1
  else:
    i+=1
    j+=1
print(ma)

#D

n = int(input())
for i in range(n):
    arr = input().strip()
    le = 0
    ri = len(arr)-1
    result = -1
    while le<= ri:
        mid = (le+ri)//2
        if arr[mid] == "1":
            result = mid+1
            ri = mid-1
        else:
            le = mid+1
    print(result)

#E

n, s = [int(x) for x in input().split(" ")]
arr = [int(x) for x in input().split(" ")]
for i in range(s):
    x, y = [int(x) for x in input().split(" ")]
    l,r = 0,n-1
    upper_bound = 0
    lower_bound = 0
    if arr[l]>= x and arr[r]<=y:
        print(n)
    elif arr[l]>y or arr[r]<x:
        print(0)
    else:
        while l <= r:
            mid = (l+r)//2
            if arr[mid] <=y:
                upper_bound = mid
                l = mid+1
            else:
                r=mid-1
        l,r = 0,n-1
        while l<= r:
            mid = (l+r)//2
            if arr[mid] <x:
                l = mid+1
            else:
                lower_bound = mid
                r = mid - 1
        print(upper_bound - lower_bound +1)
    

