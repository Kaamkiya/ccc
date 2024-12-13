hats = [int(i) for i in open('input.txt', 'r').read().splitlines()]

count = hats[0]
hats = hats[1:]

a = hats[:count//2]
b = hats[count//2:]

total = 0

for i, v in enumerate(a):
    if v == b[i]: total += 1

print(total)
