N = list(input())[::-1]
M = list(input())[::-1]

#ni = 0 # n index
#mi = 0
ne = 0 # n eaten
me = 0

while len(N) > 0 and len(M) > 0:
    # iterate over
    # for each
    #   if equal, unshift and inc neme
    #   if n>m, unshift m and inc n
    #   if m>n, unshift n and in m
    n = N.pop()
    m = M.pop()
    if n == m:
        ne += 1
        me += 1
    elif (n == "R" and m == "G" or
          n == "G" and m == "B" or
          n == "B" and m == "R"):
        ne += 1
        N.append(n)
    else:
        me += 1
        M.append(m)

ne += len(N)
me += len(M)

print(ne)
print(me)
