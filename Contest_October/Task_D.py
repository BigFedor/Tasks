n = int(input())
arg = [0] * n

for i in range(n):
    arg[i] = int(input())

def even_sort(arg):
    for i in range(len(arg)):
        for j in range(len(arg) - 1, i, -1):
            if (arg[j] % 2 == 0) and (arg[i] % 2 == 0):
                if arg[j] < arg[i]:
                    arg[j], arg[i] = arg[i], arg[j]
even_sort(arg)

for i in range(n):
    print(arg[i], end=" ")