N = int(input())
W = int(input())

weight = []
price = []

for i in range(N):
	weight.append(int(input()))
	price.append(int(input()))

summary = [[0] * (W + 1) for i in range(N + 1)]

for i in range(N):
	for j in range(W):
		if weight[i] <= j + 1:
			summary[i + 1][j + 1] = max(price[i] + summary[i][j + 1 - weight[i]], summary[i][j + 1])
		else:
			summary[i + 1][j + 1] = summary[i][j + 1]

print(summary[N][W])