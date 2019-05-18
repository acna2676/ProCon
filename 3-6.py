n = int(input())
array = []
for i in range(n):
    array.append(int(input()))# = list(map(int, input().split()))

def insertSort(array, n, g, cnt):
    for i in range(g, n):
        v = array[i]
        j = i - g
        while j >= 0 and array[j] > v:
            array[j+g] = array[j]
            j -= g
            cnt += 1
        array[j+g] = v

    return array, cnt

def shellSort(array, n):
    cnt = 0
    m = 2
    G = [4,1]
    print(m)
    print(G[0], G[1])
    for i in range(m):
        array, cnt = insertSort(array, n, G[i], cnt)
    return array, cnt
    
result, cnt = shellSort(array, n)
print(cnt)
for i in range(n):
    print(result[i])
