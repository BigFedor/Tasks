n = int(input())
altitude = []
for i in range(n):
	altitude.append(int(input()))

mine = [0] * n
mine[0] = 0
if n > 1:
	mine[1] = abs(altitude[1] - altitude[0])
if n > 2:
	for i in range(2, n):
		mine[i] = min(mine[i - 2] + 3 * abs(altitude[i] - altitude[i - 2]), mine[i - 1] + abs(altitude[i] - altitude[i - 1]))

print(mine[n - 1])
