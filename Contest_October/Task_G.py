counter = 0
n = int(input())
arg = [0] * n

for i in range(n):
    arg[i] = int(input())

m = int(input())

for i in range(n):
    if arg[m] < arg[i]:
        counter += 1

print(counter)
