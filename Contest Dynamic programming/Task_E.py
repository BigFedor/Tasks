N = int(input())

def fib(n):
    F = [-1]*(n+1)
    F[-1] = 0
    F[0] = 1
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i - 1] + F[i - 2] + F[i-3]
    return F[n]

if N <= 0:
    print(0)
else:
    res = fib(N+1)
    print(res)
