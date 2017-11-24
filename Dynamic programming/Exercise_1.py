#steps +1, +2, +3

n = int(input())
steps = [2, 4]

def grasshopper(n, steps):
	G = [0] * (n + 1)
	G[1] = 1
	for i in range(2, n + 1):
		for j in steps:
			if i-j >= 1:
				G[i] += G[i - j]
	return G[n]

print(grasshopper(n,steps))
