n = int(input())
m = 1046527
array = [1046527] * m



def h1(key):
    # print(key, type(key), m, type(m))
    # print(key % m)
    return key % m

def h2(key):
    return 1 + (key % (m-1))

def h(key, i):
    return (h1(key) + i * h2(key)) % m

def toNum(ch):
    if ch == 'A':
        return 1
    if ch == 'C':
        return 2
    if ch == 'G':
        return 3
    if ch == 'T':
        return 4
    return 0

def getKey(string):
    ch = list(string)
    sum = 0
    for i in range(len(ch)):
        # print(ch[i])
        sum += 10 ** i * toNum(ch[i])

    return sum

def insert(array, string):
    i = 0
    key = getKey(string)
    # print(string, key)
    while True:
        j = h(key, i)
        if array[j] == 1046527:
            # print(1046527)
            array[j] = key
            break
        i += 1

def find(array, key):
    i = 0
    key = getKey(string)
    while True:
        j = h(key, i)
        if array[j] == key:
            return "yes"
        if i > m:
            return "no"
        i += 1
    return "no"


for i in range(n):
    line = list(input().split())
    print(line)
    command = line[0]
    string = line[1]
    # print(command, string)

    if command == "insert":
        insert(array, string)
    elif command == "find":
        print(' ', find(array, string))

    
        

    