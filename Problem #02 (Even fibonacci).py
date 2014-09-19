n = 4000000

a, b, c = 0, 1, 0
while (c < n):
    a, b = b, a + b
    if a % 2 == 0:
        c += a
