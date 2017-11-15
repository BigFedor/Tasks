n = int(input())
enter = [0] * n
main = [0] * n
last = [0] * n

const = 0
for i in range(n):
    enter[i] = int(input())
for i in range(n):
    last[i] = enter[i]
for i in range(n):
    while last[i] > 0:
        number = last[i] % 10
        const += number
        last[i] //= 10
    main[i] = const
    const = 0

def sort(main):
    for i in range(len(main)):
        for j in range(len(main) - 1, i, -1):
            if main[j] < main[j - 1]:
                main[j], main[j - 1] = main[j - 1], main[j]
                enter[j], enter[j - 1] = enter[j - 1], enter[j]

sort(main)

for i in range(n):
    print(enter[i], end=" ")