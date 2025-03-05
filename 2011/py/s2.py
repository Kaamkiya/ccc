n = int(input())

expect = [input().strip() for _ in range(n)]
actual = [input().strip() for _ in range(n)]

c = 0

for i, s in enumerate(expect):
    if s == actual[i]: c += 1

print(c)
