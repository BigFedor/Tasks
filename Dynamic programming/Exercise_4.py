price = [0, 1, 5, 2, 3, 6, 4]

def min_cost(n, price):
    cost = [-1] * (n + 1)
    k = []
    cost[0] = price[0]
    cost[1] = price[1]
    cost[2] = price[1] + price[2]
    k.append(1)
    for i in range(3, n + 1):
        if cost[i - 1] < cost[i - 2]:
            cost[i] = cost[i - 1] + price[i]
            k.append(i - 1)
        else:
            cost[i] = cost[i - 2] + price[i]
            k.append(i - 2)

    way = []
    way.append(n)
    while way[-1] != 1:
        x = way[-1]
        way.append(k[x - 2])

    print(*way[::-1])

min_cost(6, price)