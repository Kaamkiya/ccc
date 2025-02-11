n = int(input())
scores = [int(input()) for _ in range(n)]
scores.sort()
scores.reverse()
unique = list(set(scores))
unique.sort()
unique.reverse()
print(unique[2], scores.count(unique[2]))
