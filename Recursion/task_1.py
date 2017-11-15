import sys

counter = 0
def fac(n):
    global counter
    if n == 0:
        counter += 1
        print(counter)
        return 1
    else:
        counter += 1
        return n * fac(n - 1)

print(sys.getrecursionlimit())
fac(9)

