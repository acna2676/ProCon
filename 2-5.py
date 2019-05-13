import time
from memory_profiler import profile


# #------------------------------------
# arrayA = []
# n = int(input())
# for k in range(n):
#     arrayA.append(int(input()))
# #------------------------------------

@profile
def calcFX(array):
    max = array[2] - array[1]
    for i in range(array[0]-1):
        # print('i = ', i)
        for j in range(i+2,array[0]+1):
            # print('j = ', j)
            # print('array[j] = ', array[j])
            result = array[j] - array[i+1]  
            if max < result:
                max = result

    return max


@profile
def calcFXImproved(array, n):
    max = array[1] - array[0]
    min = array[0]
    
    for i in range(1, n):
        print(max, min)
        if max < array[i] - min:
            max = array[i] - min
        if array[i] < min:
            min = array[i]

    return max

# @profile
def main():
    start = time.time()
    # arrayB = [180] + [5,3,1,3,4,3] * 30
    # arrayB = [6,5,3,1,3,4,3]
    arrayA = [5,3,1,3,4,3] * 30
    n = 180
  
    # array2 = [3,4,3,2]
    # print("result = ", calcFX(arrayB))
    print("result = ", calcFXImproved(arrayA, n))
    # print("result = ", calcFX(array2))

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':

    main()