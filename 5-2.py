n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            count += 1

print(count)

    
        

    