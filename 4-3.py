from collections import deque

array = list(map(int, input().split()))
n = array[0]
qtime = array[1]

queue = deque([])
for i in range(n):
    queue.append(int(input()))

head = 0
tail = n - 1
totalTime = 0
while queue[tail] != 0 :
    print('head = ', head, ' tail = ', tail)
    print(queue)
    if queue[head] > qtime:
        totalTime += qtime
        
        tail = (tail + 1) % n
        tmp =  queue[head] - qtime
        queue[head] = 0
        queue[tail] = tmp
        head = (head + 1) % n
    else:
        totalTime += queue[head]
        queue[head] = 0
        head = (head + 1) % n
    print(totalTime)
    
        

    