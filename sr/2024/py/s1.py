N = int(input())
hats = [int(input()) for _ in range(N)]

a = hats[:N//2]
b = hats[N//2:]

total = 0

for i, v in enumerate(a):
    if v == b[i]: total += 1

print(total)
