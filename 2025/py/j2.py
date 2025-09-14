D = int(input())
E = int(input())
R = D

for _ in range(E):
    operation = input()
    Q = int(input())

    if operation == "+":
        R += Q
    else:
        R -= Q

print(R)
