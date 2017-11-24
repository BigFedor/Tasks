#steps + 1, + 2, * 3

n = int(input())

def grasshopper(n):
	G = [-1] * (n + 1)
	G[0] = 0
	G[1] = 1
	G[2] = 1
	for i in range(3, n + 1):
		G[i] = G[i - 1] + G[i - 2]
		if i % 3 == 0:
			G[i] += G[int(i / 3)]
	return G[n]

print(grasshopper(n))