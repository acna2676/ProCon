n = int(input())
array = list(map(int, input().split()))



def selectSort(array, n):
    selectCount = 0
    minj = 0
    
    for i in range(n-1):
        min = array[i]
        minj = i
        for j in range(i+1, n):
            if min > array[j]:
                min = array[j]
                minj = j 
        
        if minj != i:
            tmp = array[i] 
            array[i] = min
            array[minj] = tmp
            selectCount += 1
        print(array)
    print(selectCount)
    return array

print(selectSort(array, n))
