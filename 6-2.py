n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))


# def makeCombination():
#     for i in range(n):

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i+1, m) or solve(i+1, m-A[i])
    return res

for i in range(q):
    if(solve(0, M[i])):
        print("yes")
    else:
        print("no")