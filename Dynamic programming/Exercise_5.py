n = int(input())
m = int(input())

set = [[0] * m for i in range(n)]

set[n - 1][m - 1] = '-'


def add_pl(set, k, l):
    for i in range(k):
        set[i][l] = '+'

    for j in range(l):
        set[k][j] = '+'

    while k > 0 and l > 0:
        k -= 1
        l -= 1
        set[k][l] = '+'


def add_min(set):
    flag = False
    for i in range(n - 1):
        for j in range(m - 1):
            if set[i][j] == 0 and set[i + 1][j + 1] == '+' and set[i][j + 1] == '+' and set[i + 1][j] == '+':
                set[i][j] = '-'
                add_pl(set, i, j)
            if set[i][j] == 0:
                flag = True

    if flag:
        add_min(set)


add_pl(set, n - 1, m - 1)
add_min(set)
