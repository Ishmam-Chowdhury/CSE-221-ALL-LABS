## A

def solve(A):
    N = len(A)
    global res
    res = 0

    def mergeSort(arr):
        if len(arr)<=1:
            return arr
        else:
            mid = len(arr)//2
            arr1 = arr[0:mid]
            arr2 = arr[mid:len(arr)]
            a1 = mergeSort(arr1)
            a2 = mergeSort(arr2)
            return merge(a1, a2)
    def merge(a,b):
        i = 0
        j= 0
        global res
        c = []
        while i<len(a) and j<len(b):
                if a[i]<b[j]:
                        c.append(a[i])
                        i+=1
                else:
                        c.append(b[j])
                        res+= len(a)-i
                        j+=1
        if i == len(a):
                c.extend(b[j:])
        
        if j == len(b):
                c.extend(a[i:])
        return c

    a = mergeSort(A)
    print(res)
    for i in a:
        print(i, end=" ")
 
n = int(input())
a = [int(x) for x in input().split(" ")]
solve(a)