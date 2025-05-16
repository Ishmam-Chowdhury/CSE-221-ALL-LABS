# A
num = int(input())
for i in range(num):
    num1= int(input())
    if num1%2==0:
        print(f"{num1} is an Even number.")
    else:
        print(f"{num1} is an Odd number.")

#Ques B

num = int(input())
for i in range(num):
    st = str(input())
    li = st.split(" ")
    num1, num2 = float(li[1]), float(li[3])
    if li[2]== "+":
        print(f"{(num1+num2):.6f}")
    elif li[2]== "-":
        print(f"{(num1-num2):.6f}")
    elif li[2]== "*":
        print(f"{(num1*num2):.6f}")
    elif li[2]== "/":
        print(f"{(num1/num2):.6f}")

#ques c

n,k = (input()).split(" ")
n, k = int(n), int(k)
arr = (input()).split(" ")
j = k-1
for i in range(j):
    print(arr[j-i], end=" ")
print(arr[0])

#ques D

S = int(input())
for i in range(S):
    N = int(input())
    sum = (N*(N+1))/2
    print(int(sum))

#ques E

def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        chang = True
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                chang = False
        if chang == True:
            break
    return arr
n= int(input())
arr = [int(i) for i in input().split(" ")]
arr = bubbleSort(arr)
for i in range(n-1):
    print(arr[i], end=" ")
print(arr[n-1])

# ques F

def swap(n,id,mark):
    s = [(id[i], mark[i]) for i in range(n)]
    swap = 0
    for i in range(n-1):
        mx = i
        for j in range(i+1,n):
            if s[mx][1]<s[j][1] or (s[j][1] == s[mx][1] and s[j][0]< s[mx][0]):
                mx = j
        if mx != i:
            s[i], s[mx] = s[mx], s[i]
            swap += 1

    print(f"Minimum swaps: {swap}")
    for i in s:
        print(f"ID: {i[0]} Mark: {i[1]}")

n = int(input())
id = [int(i) for i in input().split(" ")]
mark = [int(j) for j in input().split(" ")]

swap(n,id,mark)

#ques G

def convert_time(time):
    hour, min = time.split(":")
    net  = (int(hour)*60) + int(min)
    return net

def sort(n, li):
    for i in range(n - 1):
        for j in range(n - i - 1):
            time_j = convert_time(li[j][1])
            time_n = convert_time(li[j + 1][1])

            if li[j][0] > li[j + 1][0] or (li[j][0] == li[j + 1][0] and time_j < time_n):
                li[j], li[j + 1] = li[j + 1], li[j]

    for k in range(n):
        print(f"{li[k][0]} will departure for {li[k][2]} at {li[k][1]}")

n = int(input())
li = []
for i in range(n):
    trains = input().split()
    li.append([trains[0],trains[-1], trains[-3]])
sort(n, li)