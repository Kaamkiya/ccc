L = int(input())
m = [input().split() for _ in range(L)]
m = [(int(n[0]), n[1]) for n in m]
for l in m:
    print(l[0] * l[1])
