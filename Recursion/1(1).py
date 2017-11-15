def fac(n, counter = 0):
    if n == 0:
        print(counter)
        return 1
    elif:
        return n * fac(n - 1, counter + 1)

print(fac(2))