coordinates = input()

c = list(map(int, coordinates.split()))
c.sort()

length = [float('Inf'), c[1] - c[0]]

for i in range(2, len(c)):
	length.append(min(length[i - 2], length[i - 1]) + (c[i] - c[i - 1]))

print(length[-1])