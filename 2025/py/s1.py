A, B, X, Y = map(int, input().split(' '))

print(min(2 * (A + X + max(B, Y)),
          2 * (B + Y + max(A, X))))
