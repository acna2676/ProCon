n = int(input())
array = list(map(int, input().split()))



def bubbleSort(array, n):
    flag = 1
    changeCount = 0
    while flag:
        flag = 0
        for i in range(n-1):
            if array[i] > array[i+1]:
                flag = 1
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                changeCount += 1
    print (changeCount)
    return array

print(bubbleSort(array, n))
