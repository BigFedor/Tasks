a = int(input())
c = int(input())
b = int(input())
d = int(input())

x = abs(a - b)
y = abs(c - d)

def compare(a, b, c, d):
	if 0 < a < 9 and 0 < b < 9 and 0 < c < 9 and 0 < d < 9:
		if (x == 2 and y == 1) or (x == 1 and y == 2):
			return True

if a == b and c == d:
	print(0)
elif compare(a, b, c, d):
	print(1)
elif compare(a, c, b + 2, d + 1) or compare(a, c, b + 1, d + 2) or compare(a, c, b - 2, d - 1) or compare(a, c, b - 1, d - 2) or compare(a, c, b + 2, d - 1) or compare(a, c, b - 2, d + 1) or compare(a, c, b - 1, d + 2) or compare(a, c, b + 1, d - 2):
	print(2)
else:
	print(-1)