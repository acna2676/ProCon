n = int(input())
array = list(map(int, input().split()))


def insertSort(array, n):
    for i in range(1, n):
        v = array[i]
        j = i - 1
        while j >= 0 and array[j] > v:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = v

        print(array)
    return array




insertSort(array, n)