array = []
array = input().split()
print(array)
stack = []
operator = ['+', '-', '*', '/']

for i in range(len(array)):
    if array[i] not in operator:
        stack.append(array[i])
    if array[i] in operator:
        b = stack.pop()
        a = stack.pop()
    if array[i] == '+':
        stack.append(int(a) + int(b))
    if array[i] == '-':
        stack.append(int(a) - int(b))
    if array[i] == '*':
        stack.append(int(a) * int(b))
    if array[i] == '/':
        stack.append(int(a) / int(b))

print(stack[0])