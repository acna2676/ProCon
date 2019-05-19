n = int(input())
arrayOriginal = list(input().split())

array  = []
# d = {}
for i in range(len(arrayOriginal)):
    array.append(int(arrayOriginal[i][1:2]))
    # num = int(arrayOriginal[i][1:2])
    # d.update(num = arrayOriginal[i])


# print(d, num)

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
    # print (changeCount)
    return array

print(bubbleSort(array, n))

result = []
for j in array:
    result.append(arrayOriginal[j])

print(result)