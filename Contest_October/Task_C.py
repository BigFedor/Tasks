n = int(input())
first = [0] * n
second = [0] * n

for i in range(n):
    first[i] = int(input())
for i in range(n):
    second[i] = int(input())

def sort(first):
    for i in range(len(first)):
        for j in range(len(first) - 1, i, -1):
            if first[j] < first[j-1]:
                first[j], first[j-1] = first[j-1], first[j]
                second[j], second[j - 1] = second[j - 1], second[j]
            elif first[j] == first[j - 1]:
                second[j], second[j - 1] = second[j - 1], second[j]
    return sort

sort(first)

for i in range(n):
    print(first[i], end=" ")

print()

for i in range(n):
    print(second[i], end=" ")