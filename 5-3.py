def binarySearch(S, key, n):
    left = 0
    right = n -1 
    while left < right:
        mid = int((left + right) / 2) 
        print("left = ", left, " mid = ", mid, " right = ", right)
        print("S[mid] = ", S[mid], " key = ", key)
        if S[mid] == key:
            return mid
        elif S[mid] > key:
            right = mid
        else:
            left = mid + 1
    return -1

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for i in range(len(T)):
    res = binarySearch(S, T[i], n)
    if res > -1:
        count += 1
    print("i = ", i, " res = ", res)

print(count)

    
        

    