n = int(input())
p = [[int(i) for i in input().split(',')] for _ in range(n)]

c1 = [min([x[0] for x in p]) - 1, min([x[1] for x in p]) - 1]
c2 = [max([x[0] for x in p]) + 1, max([x[1] for x in p]) + 1]

print('{},{}'.format(*c1))
print('{},{}'.format(*c2))
