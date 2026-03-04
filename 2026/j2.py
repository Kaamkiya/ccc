S = [int(input()) for _ in range(5)]
S.remove(max(S))
S.remove(min(S))
D = int(input())

print(sum(S) * D)
