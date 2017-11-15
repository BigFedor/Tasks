n = int(input())
arg = [0] * n

def sort(arg):
    for i in range(len(arg)):
        for j in range(len(arg) - 1, i, -1):
            if arg[j] < arg[j-1]:
                arg[j], arg[j-1] = arg[j-1], arg[j]

    return arg

for i in range(n):
    arg[i] = int(input())

sort(arg)

for i in range(len(arg)):
    print(arg[i], end=' ')