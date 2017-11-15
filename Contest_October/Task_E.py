n = int(input())
m = int(input())
arg = [0] * (n * m)

for i in range(n * m):
    arg[i] = int(input())

def sort(arg):
    for i in range(len(arg)):
        for j in range(len(arg) - 1, i, -1):
            if arg[j] < arg[j - 1]:
                arg[j], arg[j - 1] = arg[j - 1], arg[j]

sort(arg)

const = 0
for i in range(m * n):
    print(arg[i], end=" ")
    const += 1
    if const == m:
        print()
        const = 0
